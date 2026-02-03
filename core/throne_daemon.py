#!/usr/bin/env python3
"""
THE THRONE - Auto-Processing Daemon
Continuous monitoring and processing with REST API endpoint
"""
import os
import time
import threading
import json
from pathlib import Path
from datetime import datetime

try:
    from flask import Flask, jsonify, request
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False
    print("Warning: Flask not installed. API will not be available.")

# ========================================================================
# PATHS
# ========================================================================
ROOT = Path.home() / "KINGDOM_ENGINE"
INBOX = ROOT / "inbox"
LOGS = ROOT / "logs"
PROCESSED = ROOT / "processed"
CORE = Path(__file__).parent

if FLASK_AVAILABLE:
    app = Flask("throne")
else:
    app = None

# ========================================================================
# STATE
# ========================================================================
state = {
    "running": True,
    "processed_count": 0,
    "last_run": 0,
    "errors": [],
    "start_time": time.time()
}

# ========================================================================
# LOGGING
# ========================================================================
def log_msg(msg, level="INFO"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] [{level}] {msg}"
    print(line)
    log_file = LOGS / "throne.log"
    with open(log_file, "a") as f:
        f.write(line + "\n")

# ========================================================================
# DAEMON LOOP
# ========================================================================
def daemon_loop():
    """Continuously process inbox"""
    processor_script = CORE / "hardcore_processor.py"
    
    log_msg("THRONE DAEMON STARTED", "INFO")
    
    while state["running"]:
        try:
            # Count files in inbox
            inbox_files = list(INBOX.glob("*"))
            inbox_count = len([f for f in inbox_files if f.is_file() and not f.name.startswith(".")])
            
            if inbox_count > 0:
                log_msg(f"Processing {inbox_count} files from inbox", "INFO")
                # Run processor
                os.system(f"python3 {processor_script}")
                state["processed_count"] += inbox_count
                state["last_run"] = time.time()
            
            # Sleep
            time.sleep(2)
            
        except Exception as e:
            error_msg = {
                "time": time.time(),
                "error": str(e)
            }
            state["errors"].append(error_msg)
            log_msg(f"DAEMON ERROR: {e}", "ERROR")
            time.sleep(5)

# ========================================================================
# API ENDPOINTS
# ========================================================================
if FLASK_AVAILABLE:
    @app.route("/status")
    def status():
        """Get daemon status"""
        try:
            accepted = list((PROCESSED / "accepted").glob("*.txt"))
            quarantine = list((PROCESSED / "quarantine").glob("*.txt"))
            
            uptime = time.time() - state["start_time"]
            
            return jsonify({
                "status": "running" if state["running"] else "stopped",
                "processed_total": state["processed_count"],
                "last_run": state["last_run"],
                "uptime_seconds": int(uptime),
                "inbox_count": len(list(INBOX.glob("*.txt"))),
                "accepted_count": len(accepted),
                "quarantine_count": len(quarantine),
                "errors_recent": state["errors"][-10:]
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/stop", methods=["POST"])
    def stop():
        """Stop the daemon"""
        state["running"] = False
        log_msg("DAEMON STOP REQUESTED", "INFO")
        return jsonify({"status": "stopping"})

    @app.route("/start", methods=["POST"])
    def start():
        """Start the daemon"""
        state["running"] = True
        log_msg("DAEMON START REQUESTED", "INFO")
        return jsonify({"status": "starting"})

    @app.route("/accepted")
    def get_accepted():
        """List accepted files"""
        files = []
        try:
            for f in (PROCESSED / "accepted").glob("*.meta.json"):
                try:
                    with open(f) as fp:
                        meta = json.load(fp)
                        files.append(meta)
                except:
                    pass
        except:
            pass
        return jsonify(files)

    @app.route("/quarantine")
    def get_quarantine():
        """List quarantined files"""
        files = []
        try:
            for f in (PROCESSED / "quarantine").glob("*.meta.json"):
                try:
                    with open(f) as fp:
                        meta = json.load(fp)
                        files.append(meta)
                except:
                    pass
        except:
            pass
        return jsonify(files)

    @app.route("/logs")
    def get_logs():
        """Get recent logs"""
        log_file = LOGS / "throne.log"
        lines = []
        try:
            if log_file.exists():
                with open(log_file) as f:
                    lines = f.readlines()[-100:]  # Last 100 lines
        except:
            pass
        return jsonify({"logs": lines})

# ========================================================================
# MAIN
# ========================================================================
if __name__ == "__main__":
    # Create directories
    for d in [INBOX, LOGS, PROCESSED / "accepted", PROCESSED / "quarantine"]:
        d.mkdir(parents=True, exist_ok=True)
    
    # Start daemon thread
    daemon = threading.Thread(target=daemon_loop, daemon=True)
    daemon.start()
    
    log_msg("THE THRONE INITIALIZED", "INFO")
    
    if FLASK_AVAILABLE:
        log_msg("Starting API on http://127.0.0.1:5200", "INFO")
        app.run(host="127.0.0.1", port=5200, debug=False, use_reloader=False)
    else:
        log_msg("Flask not available - running daemon only", "WARN")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            state["running"] = False
            log_msg("THRONE SHUTDOWN", "INFO")
