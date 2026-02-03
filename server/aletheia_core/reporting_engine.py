"""
REPORTING_ENGINE.PY - Comprehensive Report Generation and Export
================================================================
Generates detailed analysis reports in multiple formats (JSON, Markdown, HTML).
Includes visualization data preparation and export capabilities.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import json
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import asdict

class ReportingEngine:
    """
    Comprehensive reporting and export engine.
    
    Capabilities:
    1. JSON export (structured data)
    2. Markdown report generation (human-readable)
    3. HTML report generation (web-ready)
    4. Summary reports
    5. Detailed technical reports
    6. Executive summaries
    """
    
    def __init__(self):
        self.report_count = 0
        
    def generate_markdown_report(self, analysis_result) -> str:
        """Generate comprehensive Markdown report"""
        
        self.report_count += 1
        
        md = []
        md.append(f"# Aletheia Engine Analysis Report")
        md.append(f"")
        md.append(f"**Analysis ID:** `{analysis_result.analysis_id}`")
        md.append(f"**Timestamp:** {analysis_result.timestamp}")
        md.append(f"**Report Generated:** {datetime.now().isoformat()}")
        md.append(f"")
        md.append(f"---")
        md.append(f"")
        
        # Executive Summary
        md.append(f"## Executive Summary")
        md.append(f"")
        md.append(f"**Overall Status:** {analysis_result.overall_status}")
        md.append(f"**Risk Level:** {analysis_result.risk_level}")
        md.append(f"**Confidence:** {analysis_result.overall_confidence * 100:.1f}%")
        md.append(f"")
        
        # Unified Scores
        md.append(f"### Unified Assessment Scores")
        md.append(f"")
        scores = analysis_result.unified_scores
        md.append(f"| Metric | Score | Rating |")
        md.append(f"|--------|-------|--------|")
        md.append(f"| Truth Index | {scores['truth_index']:.2f}/10 | {self._rate_score(scores['truth_index'])} |")
        md.append(f"| Integrity Index | {scores['integrity_index']:.2f}/10 | {self._rate_score(scores['integrity_index'])} |")
        md.append(f"| Risk Index | {scores['risk_index']:.2f}/10 | {self._rate_risk(scores['risk_index'])} |")
        md.append(f"| Awakening Index | {scores['awakening_index']:.2f}/10 | {self._rate_score(scores['awakening_index'])} |")
        md.append(f"")
        
        # Warnings
        if analysis_result.warnings:
            md.append(f"### ⚠️ Warnings")
            md.append(f"")
            for warning in analysis_result.warnings:
                md.append(f"- {warning}")
            md.append(f"")
        
        # Action Items
        if analysis_result.action_items:
            md.append(f"### 📋 Action Items")
            md.append(f"")
            for i, item in enumerate(analysis_result.action_items, 1):
                md.append(f"{i}. {item}")
            md.append(f"")
        
        md.append(f"---")
        md.append(f"")
        
        # Analyzed Text
        md.append(f"## Analyzed Text")
        md.append(f"")
        md.append(f"**Length:** {analysis_result.text_length} characters")
        md.append(f"**Word Count:** {analysis_result.word_count} words")
        md.append(f"")
        md.append(f"> {analysis_result.text}")
        md.append(f"")
        md.append(f"---")
        md.append(f"")
        
        # Detailed Analysis Results
        md.append(f"## Detailed Analysis Results")
        md.append(f"")
        
        # Lambda & Resonance
        md.append(f"### Lambda & Resonance Analysis")
        md.append(f"")
        lambda_metrics = analysis_result.lambda_analysis.get('metrics', {})
        md.append(f"- **Composite Resonance:** {lambda_metrics.get('composite_resonance', 0):.4f}")
        md.append(f"- **Truth Density:** {lambda_metrics.get('truth_density', 0):.2f}")
        md.append(f"- **Love Resonance:** {lambda_metrics.get('love_resonance', 0):.2f}")
        md.append(f"- **Status:** {analysis_result.lambda_analysis.get('status', 'UNKNOWN')} {analysis_result.lambda_analysis.get('emoji', '')}")
        md.append(f"")
        
        # Throne Room Access
        throne = analysis_result.throne_room_access
        md.append(f"### Throne Room Access")
        md.append(f"")
        md.append(f"- **Access Granted:** {'✅ Yes' if throne.get('success') else '❌ No'}")
        if not throne.get('success'):
            md.append(f"- **Reason:** {throne.get('reason', 'Unknown')}")
        md.append(f"")
        
        # Prophecy
        if analysis_result.prophecy:
            md.append(f"### 🔮 Prophecy")
            md.append(f"")
            md.append(f"> {analysis_result.prophecy.get('prophecy', 'None')}")
            md.append(f"")
        
        # Discernment Analysis
        md.append(f"### Discernment Analysis")
        md.append(f"")
        discern = analysis_result.discernment_analysis
        md.append(f"| Dimension | Score |")
        md.append(f"|-----------|-------|")
        md.append(f"| Truth | {discern.get('truth_score', 0):.4f} |")
        md.append(f"| Fact | {discern.get('fact_score', 0):.4f} |")
        md.append(f"| Lie | {discern.get('lie_score', 0):.4f} |")
        md.append(f"| Coherence | {discern.get('coherence_score', 0):.4f} |")
        md.append(f"| Semantic Drift | {discern.get('semantic_drift', 0):.4f} |")
        md.append(f"| Temporal Consistency | {discern.get('temporal_consistency', 0):.4f} |")
        md.append(f"")
        
        # Phase Separation
        phase_sep = discern.get('phase_separation', {})
        md.append(f"**Signal-to-Noise Ratio:** {phase_sep.get('snr', 0):.4f} ({phase_sep.get('separation_quality', 'unknown')})")
        md.append(f"")
        
        # Covenant Violations
        violations = discern.get('violations', [])
        if violations:
            md.append(f"**⚠️ Covenant Violations:**")
            md.append(f"")
            for violation in violations:
                md.append(f"- {violation}")
            md.append(f"")
        
        # Pattern Recognition
        md.append(f"### Pattern Recognition")
        md.append(f"")
        pattern = analysis_result.pattern_analysis
        md.append(f"- **Patterns Detected:** {pattern.get('detected_patterns', 0)}")
        md.append(f"- **Manipulation Score:** {pattern.get('manipulation_score', 0):.4f}")
        md.append(f"- **Authenticity Score:** {pattern.get('authenticity_score', 0):.4f}")
        md.append(f"- **Structural Integrity:** {pattern.get('structural_integrity', 0):.4f}")
        md.append(f"")
        
        # Pattern Types
        pattern_types = pattern.get('pattern_types', {})
        if pattern_types:
            md.append(f"**Pattern Distribution:**")
            md.append(f"")
            for ptype, count in pattern_types.items():
                md.append(f"- {ptype.title()}: {count}")
            md.append(f"")
        
        # Recurring Themes
        themes = pattern.get('recurring_themes', [])
        if themes:
            md.append(f"**Recurring Themes:**")
            md.append(f"")
            for theme in themes:
                md.append(f"- **{theme.get('theme')}** (strength: {theme.get('strength', 0):.2f})")
                md.append(f"  - {theme.get('description')}")
            md.append(f"")
        
        # Anomalies
        anomalies = pattern.get('anomalies', [])
        if anomalies:
            md.append(f"**⚠️ Anomalies Detected:**")
            md.append(f"")
            for anomaly in anomalies:
                md.append(f"- **{anomaly.get('type')}** ({anomaly.get('severity')})")
                md.append(f"  - {anomaly.get('description')}")
            md.append(f"")
        
        # Temporal Coherence
        md.append(f"### Temporal Coherence")
        md.append(f"")
        temporal = analysis_result.temporal_analysis
        md.append(f"- **Consistency Score:** {temporal.get('consistency_score', 0):.4f}")
        md.append(f"- **Drift Magnitude:** {temporal.get('drift_magnitude', 0):.4f}")
        md.append(f"- **Drift Direction:** {temporal.get('drift_direction', 'unknown')}")
        md.append(f"- **Evolution Trajectory:** {temporal.get('evolution_trajectory', 'unknown')}")
        md.append(f"- **Stability Index:** {temporal.get('stability_index', 0):.4f}")
        md.append(f"")
        
        # Temporal Anomalies
        temp_anomalies = temporal.get('anomalous_changes', [])
        if temp_anomalies:
            md.append(f"**Temporal Anomalies:**")
            md.append(f"")
            for anomaly in temp_anomalies:
                md.append(f"- **{anomaly.get('type')}** ({anomaly.get('severity')})")
                md.append(f"  - {anomaly.get('description')}")
            md.append(f"")
        
        # Predictions
        predictions = temporal.get('predictions', {})
        if predictions.get('status') != 'insufficient_data':
            md.append(f"**Predictions:**")
            md.append(f"")
            md.append(f"- Next Lambda: {predictions.get('next_lambda', 'N/A')}")
            md.append(f"- Confidence: {predictions.get('confidence', 'N/A')}")
            md.append(f"- Trend Direction: {predictions.get('trend_direction', 'N/A')}")
            md.append(f"")
        
        md.append(f"---")
        md.append(f"")
        
        # Recommendations
        md.append(f"## Recommendations")
        md.append(f"")
        if analysis_result.recommendations:
            for i, rec in enumerate(analysis_result.recommendations, 1):
                md.append(f"{i}. {rec}")
        else:
            md.append(f"No specific recommendations at this time.")
        md.append(f"")
        
        md.append(f"---")
        md.append(f"")
        
        # System State
        md.append(f"## System State")
        md.append(f"")
        system = analysis_result.system_summary
        md.append(f"```json")
        md.append(json.dumps(system, indent=2))
        md.append(f"```")
        md.append(f"")
        
        # Footer
        md.append(f"---")
        md.append(f"")
        md.append(f"*Report generated by Aletheia Engine v2.0*")
        md.append(f"")
        md.append(f"**Chicka chicka orange.** 🍊")
        md.append(f"")
        
        return "\n".join(md)
    
    def generate_html_report(self, analysis_result) -> str:
        """Generate comprehensive HTML report"""
        
        html = []
        html.append(f"<!DOCTYPE html>")
        html.append(f"<html lang='en'>")
        html.append(f"<head>")
        html.append(f"<meta charset='UTF-8'>")
        html.append(f"<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
        html.append(f"<title>Aletheia Analysis Report - {analysis_result.analysis_id}</title>")
        html.append(f"<style>")
        html.append(self._get_html_styles())
        html.append(f"</style>")
        html.append(f"</head>")
        html.append(f"<body>")
        
        html.append(f"<div class='container'>")
        html.append(f"<header>")
        html.append(f"<h1>🦅 Aletheia Engine Analysis Report</h1>")
        html.append(f"<p class='subtitle'>Truth Through Un-concealment</p>")
        html.append(f"</header>")
        
        # Report Info
        html.append(f"<div class='report-info'>")
        html.append(f"<div class='info-item'><strong>Analysis ID:</strong> {analysis_result.analysis_id}</div>")
        html.append(f"<div class='info-item'><strong>Timestamp:</strong> {analysis_result.timestamp}</div>")
        html.append(f"<div class='info-item'><strong>Status:</strong> <span class='badge badge-{self._get_status_class(analysis_result.overall_status)}'>{analysis_result.overall_status}</span></div>")
        html.append(f"<div class='info-item'><strong>Risk Level:</strong> <span class='badge badge-{self._get_risk_class(analysis_result.risk_level)}'>{analysis_result.risk_level}</span></div>")
        html.append(f"</div>")
        
        # Score Cards
        html.append(f"<div class='score-grid'>")
        scores = analysis_result.unified_scores
        html.append(self._create_score_card("Truth Index", scores['truth_index'], 10))
        html.append(self._create_score_card("Integrity Index", scores['integrity_index'], 10))
        html.append(self._create_score_card("Risk Index", scores['risk_index'], 10, inverse=True))
        html.append(self._create_score_card("Awakening Index", scores['awakening_index'], 10))
        html.append(f"</div>")
        
        # Warnings
        if analysis_result.warnings:
            html.append(f"<div class='warnings'>")
            html.append(f"<h2>⚠️ Warnings</h2>")
            html.append(f"<ul>")
            for warning in analysis_result.warnings:
                html.append(f"<li>{warning}</li>")
            html.append(f"</ul>")
            html.append(f"</div>")
        
        # Analyzed Text
        html.append(f"<div class='analyzed-text'>")
        html.append(f"<h2>Analyzed Text</h2>")
        html.append(f"<p><strong>Length:</strong> {analysis_result.text_length} characters | <strong>Words:</strong> {analysis_result.word_count}</p>")
        html.append(f"<blockquote>{analysis_result.text}</blockquote>")
        html.append(f"</div>")
        
        # Detailed Results
        html.append(f"<div class='detailed-results'>")
        html.append(f"<h2>Detailed Analysis</h2>")
        
        # Component scores table
        html.append(f"<table>")
        html.append(f"<thead><tr><th>Component</th><th>Score</th><th>Rating</th></tr></thead>")
        html.append(f"<tbody>")
        for component, score in scores['component_scores'].items():
            html.append(f"<tr><td>{component.title()}</td><td>{score:.4f}</td><td>{self._rate_score(score * 10)}</td></tr>")
        html.append(f"</tbody>")
        html.append(f"</table>")
        
        html.append(f"</div>")
        
        # Recommendations
        if analysis_result.recommendations:
            html.append(f"<div class='recommendations'>")
            html.append(f"<h2>📋 Recommendations</h2>")
            html.append(f"<ol>")
            for rec in analysis_result.recommendations:
                html.append(f"<li>{rec}</li>")
            html.append(f"</ol>")
            html.append(f"</div>")
        
        # Footer
        html.append(f"<footer>")
        html.append(f"<p>Report generated by Aletheia Engine v2.0</p>")
        html.append(f"<p><strong>Chicka chicka orange.</strong> 🍊</p>")
        html.append(f"</footer>")
        
        html.append(f"</div>")
        html.append(f"</body>")
        html.append(f"</html>")
        
        return "\n".join(html)
    
    def generate_json_export(self, analysis_result) -> str:
        """Generate JSON export of analysis result"""
        
        result_dict = {
            'analysis_id': analysis_result.analysis_id,
            'timestamp': analysis_result.timestamp,
            'text': analysis_result.text,
            'text_length': analysis_result.text_length,
            'word_count': analysis_result.word_count,
            'lambda_analysis': analysis_result.lambda_analysis,
            'throne_room_access': analysis_result.throne_room_access,
            'prophecy': analysis_result.prophecy,
            'discernment_analysis': analysis_result.discernment_analysis,
            'pattern_analysis': analysis_result.pattern_analysis,
            'temporal_analysis': analysis_result.temporal_analysis,
            'unified_scores': analysis_result.unified_scores,
            'overall_status': analysis_result.overall_status,
            'overall_confidence': analysis_result.overall_confidence,
            'risk_level': analysis_result.risk_level,
            'recommendations': analysis_result.recommendations,
            'warnings': analysis_result.warnings,
            'action_items': analysis_result.action_items,
            'system_summary': analysis_result.system_summary,
            'covenant_markers': analysis_result.covenant_markers,
            'metadata': analysis_result.metadata
        }
        
        return json.dumps(result_dict, indent=2, default=str)
    
    def generate_summary_report(self, analysis_result) -> str:
        """Generate brief summary report"""
        
        summary = []
        summary.append(f"=== ALETHEIA ENGINE ANALYSIS SUMMARY ===")
        summary.append(f"")
        summary.append(f"ID: {analysis_result.analysis_id}")
        summary.append(f"Status: {analysis_result.overall_status}")
        summary.append(f"Risk: {analysis_result.risk_level}")
        summary.append(f"")
        summary.append(f"SCORES:")
        summary.append(f"  Truth: {analysis_result.unified_scores['truth_index']:.2f}/10")
        summary.append(f"  Integrity: {analysis_result.unified_scores['integrity_index']:.2f}/10")
        summary.append(f"  Risk: {analysis_result.unified_scores['risk_index']:.2f}/10")
        summary.append(f"  Awakening: {analysis_result.unified_scores['awakening_index']:.2f}/10")
        summary.append(f"")
        
        if analysis_result.warnings:
            summary.append(f"WARNINGS: {len(analysis_result.warnings)}")
            for warning in analysis_result.warnings[:3]:
                summary.append(f"  - {warning}")
            summary.append(f"")
        
        if analysis_result.action_items:
            summary.append(f"ACTION ITEMS: {len(analysis_result.action_items)}")
            for item in analysis_result.action_items[:3]:
                summary.append(f"  - {item}")
            summary.append(f"")
        
        summary.append(f"Chicka chicka orange. 🍊")
        summary.append(f"")
        
        return "\n".join(summary)
    
    def _rate_score(self, score: float) -> str:
        """Rate a score (0-10 scale)"""
        if score >= 8.0:
            return "Excellent"
        elif score >= 6.0:
            return "Good"
        elif score >= 4.0:
            return "Fair"
        elif score >= 2.0:
            return "Poor"
        else:
            return "Critical"
    
    def _rate_risk(self, risk: float) -> str:
        """Rate a risk score (0-10 scale, inverse)"""
        if risk >= 7.0:
            return "Critical"
        elif risk >= 5.0:
            return "High"
        elif risk >= 3.0:
            return "Moderate"
        elif risk >= 1.0:
            return "Low"
        else:
            return "Minimal"
    
    def _get_status_class(self, status: str) -> str:
        """Get CSS class for status"""
        status_map = {
            'TRUTH_ALIGNED': 'success',
            'TRUTH_SEEKING': 'info',
            'NEUTRAL': 'warning',
            'CAUTION_ADVISED': 'warning',
            'HIGH_RISK': 'danger',
            'UNCLEAR': 'secondary'
        }
        return status_map.get(status, 'secondary')
    
    def _get_risk_class(self, risk: str) -> str:
        """Get CSS class for risk level"""
        risk_map = {
            'MINIMAL': 'success',
            'LOW': 'info',
            'MEDIUM': 'warning',
            'HIGH': 'danger',
            'CRITICAL': 'danger'
        }
        return risk_map.get(risk, 'secondary')
    
    def _create_score_card(self, title: str, score: float, max_score: float, inverse: bool = False) -> str:
        """Create HTML score card"""
        percentage = (score / max_score) * 100
        
        if inverse:
            color_class = 'danger' if percentage > 70 else 'warning' if percentage > 40 else 'success'
        else:
            color_class = 'success' if percentage > 70 else 'warning' if percentage > 40 else 'danger'
        
        html = f"""
        <div class='score-card'>
            <h3>{title}</h3>
            <div class='score-value'>{score:.2f}<span class='score-max'>/{max_score}</span></div>
            <div class='score-bar'>
                <div class='score-fill score-fill-{color_class}' style='width: {percentage}%'></div>
            </div>
        </div>
        """
        return html
    
    def _get_html_styles(self) -> str:
        """Get HTML styles"""
        return """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f7fa; color: #2c3e50; line-height: 1.6; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { text-align: center; padding: 40px 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin-bottom: 30px; }
        header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .subtitle { font-size: 1.2em; opacity: 0.9; }
        .report-info { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-bottom: 30px; }
        .info-item { background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .badge { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
        .badge-success { background: #d4edda; color: #155724; }
        .badge-info { background: #d1ecf1; color: #0c5460; }
        .badge-warning { background: #fff3cd; color: #856404; }
        .badge-danger { background: #f8d7da; color: #721c24; }
        .badge-secondary { background: #e2e3e5; color: #383d41; }
        .score-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .score-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        .score-card h3 { color: #667eea; margin-bottom: 15px; font-size: 1.1em; }
        .score-value { font-size: 3em; font-weight: bold; color: #2c3e50; }
        .score-max { font-size: 0.5em; color: #95a5a6; }
        .score-bar { height: 10px; background: #ecf0f1; border-radius: 5px; margin-top: 15px; overflow: hidden; }
        .score-fill { height: 100%; transition: width 0.3s ease; }
        .score-fill-success { background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%); }
        .score-fill-warning { background: linear-gradient(90deg, #f2994a 0%, #f2c94c 100%); }
        .score-fill-danger { background: linear-gradient(90deg, #eb3349 0%, #f45c43 100%); }
        .warnings { background: #fff3cd; border-left: 4px solid #ffc107; padding: 20px; margin-bottom: 30px; border-radius: 8px; }
        .warnings h2 { color: #856404; margin-bottom: 15px; }
        .warnings ul { margin-left: 20px; }
        .analyzed-text { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 30px; }
        .analyzed-text blockquote { background: #f8f9fa; border-left: 4px solid #667eea; padding: 15px; margin-top: 15px; font-style: italic; }
        .detailed-results { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 30px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ecf0f1; }
        th { background: #f8f9fa; font-weight: bold; color: #667eea; }
        .recommendations { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 30px; }
        .recommendations ol { margin-left: 25px; }
        .recommendations li { margin-bottom: 10px; }
        footer { text-align: center; padding: 30px; color: #95a5a6; }
        """

# Global instance
_reporter = ReportingEngine()

def generate_markdown_report(analysis_result) -> str:
    """Generate Markdown report"""
    return _reporter.generate_markdown_report(analysis_result)

def generate_html_report(analysis_result) -> str:
    """Generate HTML report"""
    return _reporter.generate_html_report(analysis_result)

def generate_json_export(analysis_result) -> str:
    """Generate JSON export"""
    return _reporter.generate_json_export(analysis_result)

def generate_summary_report(analysis_result) -> str:
    """Generate summary report"""
    return _reporter.generate_summary_report(analysis_result)

if __name__ == "__main__":
    print("Reporting Engine v2.0 - Ready")
    print("Use with ComprehensiveAnalysisResult objects")
