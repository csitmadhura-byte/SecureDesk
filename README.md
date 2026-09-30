# SecureDesk — IT Support & Endpoint Security Monitoring System

SecureDesk is a Python-based Windows IT support and endpoint security monitoring system developed as a cybersecurity portfolio project.

The system combines common IT support diagnostics with basic endpoint security monitoring to help identify system health issues, network problems, resource usage, Windows security events, and firewall configuration.

---

## Project Overview

SecureDesk provides a command-line interface for performing several Windows system and security checks from a single application.

The project was developed using Python and Windows PowerShell commands, with SQLite used to maintain scan history and HTML used to generate security reports.

### Main Objectives

- Monitor Windows system health
- Perform basic network diagnostics
- Monitor running processes
- Check disk usage
- Analyze Windows Security Events
- Detect repeated failed login attempts
- Check Windows Firewall profiles
- Maintain scan history
- Generate HTML security reports
- Provide rule-based security recommendations
- Maintain application logs
- Perform automated module testing

---

## Key Features

### 1. System Information

SecureDesk collects important system information including:

- Hostname:DESKTOP-T7OMJSR
- Operating system:Windows
- OS version: 10.0.26300
- System architecture:AMD64
- Processor information:Intel64 Family 6 Model 186 Stepping 2, GenuineIntel
- CPU usage: 10.2 %
- Memory usage:58.1 %
- Disk usage:14.3 %

---

### 2. Network Diagnostics

SecureDesk performs basic network diagnostics including:

- Hostname detection : DESKTOP-T7OMJSR
- Local IP detection : 192.168.56.1
- Internet connectivity : FAIL
- DNS resolution : PASS

The application uses a controlled ping test and DNS lookup to perform these checks.

---

### 3. Process Monitoring

SecureDesk displays the top running processes based on CPU usage.

Information includes:

- Process ID
- Process name
- CPU usage
- Memory usage

This can help identify resource-intensive processes that may require further investigation.

> **Note:** A process using high CPU or having an unfamiliar name is not automatically malicious. SecureDesk reports system information for investigation rather than claiming malware detection.

---

### 4. Disk Health Monitoring

SecureDesk checks the primary Windows drive and reports:

- Total disk space : 475.90 GB
- Used space :68.23 GB
- Free space :407.67 GB
- Disk usage percentage : 14.3%
- Health status: PASS

The system uses configured thresholds to identify normal, warning, and critical disk usage.

---

### 5. Windows Security Event Analysis

SecureDesk analyzes Windows Security Event Log information using:

- Event ID 4624 — Successful Logon
- Event ID 4625 — Failed Logon

The current implementation analyzes the previous 24 hours.

A configurable threshold is used to identify an unusual number of failed login attempts.

Example:

```text
Successful Logins (4624): 0
Failed Logins (4625): 0
Threshold: 5
Status: PASS
```

A warning is generated when the number of failed login attempts reaches or exceeds the configured threshold.

The result is intended as an indicator for further investigation and does not by itself prove malicious activity.

---

### 6. Windows Firewall Monitoring

SecureDesk checks Windows Firewall profiles using PowerShell.

The application checks detected profiles such as:

- Domain
- Private
- Public

Example:

```text
Domain: ENABLED
Private: ENABLED
Public: ENABLED

Overall Status: PASS
```

The system reports a warning when one or more detected firewall profiles are disabled.

---

### 7. Logging

SecureDesk maintains an application log at:

```text
logs/securedesk.log
```

The logging system records:

- Application startup
- Completed checks
- Warnings
- Errors
- Application shutdown
- Invalid menu selections

---

### 8. SQLite Scan History

SecureDesk stores scan results in:

```text
logs/securedesk.db
```

The SQLite database maintains:

- Scan ID
- Scan type
- Status
- Details
- Timestamp

The application can display the latest scan records from the main menu.

Example:

```text
SECUREDESK SCAN HISTORY

Scan ID    : 14
Scan Type  : Windows Firewall
Status     : PASS
Details    : All detected Windows Firewall profiles are enabled.
Timestamp  : 2026-09-30 17:53:17
```

---

### 9. HTML Security Report

SecureDesk can generate an HTML security report containing:

- System information
- Network diagnostics
- Disk health
- Windows Security Events
- Windows Firewall status
- Security recommendations
- Scan history
- Report generation timestamp

The generated report is stored at:

```text
reports/securedesk_report.html
```

The application can automatically open the report in the default web browser.

---

### 10. Security Recommendations

SecureDesk generates rule-based security recommendations based on collected system information.

Recommendations can relate to:

- High disk usage
- Internet connectivity
- DNS failures
- Failed login attempts
- Firewall configuration
- High CPU usage
- High memory usage

These recommendations are intended to support basic IT troubleshooting and security investigation.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| psutil | System and process monitoring |
| PowerShell | Windows security and firewall queries |
| SQLite | Scan history storage |
| HTML/CSS | Security report generation |
| Python Logging | Application logging |
| Windows Event Log | Security event analysis |
| Git/GitHub | Version control and project hosting |

---

## Project Structure

```text
secure desk/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── system_info.py
│   ├── network_check.py
│   ├── process_monitor.py
│   ├── disk_health.py
│   ├── event_analyzer.py
│   ├── firewall_check.py
│   ├── logger.py
│   ├── database.py
│   └── report_generator.py
│
├── reports/
│   └── securedesk_report.html
│
├── logs/
│   ├── securedesk.log
│   └── securedesk.db
│
└── tests/
    └── test_modules.py
```

---

## How SecureDesk Works

The application follows this general workflow:

```text
                    ┌───────────────────┐
                    │     SecureDesk    │
                    │     main.py       │
                    └─────────┬─────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
      System Monitoring  Network Checks  Security Monitoring
             │                │                │
             │                │        ┌───────┴────────┐
             │                │        │                │
             ▼                ▼        ▼                ▼
          psutil          Socket/Ping  Event Logs    Firewall
             │                │        4624/4625    PowerShell
             └────────────────┼───────────────┬────────┘
                              │               │
                              ▼               ▼
                         Scan Results     Recommendations
                              │               │
                              └───────┬───────┘
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                    SQLite History             HTML Report
                         │                         │
                         ▼                         ▼
                  logs/securedesk.db      reports/securedesk_report.html
```

---

## Installation

### Requirements

- Windows operating system
- Python 3.x
- PowerShell
- Internet connection for network diagnostics

### 1. Clone the Repository

```powershell
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Open the Project

```powershell
cd "secure desk"
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run SecureDesk

```powershell
python main.py
```

---

## Main Menu

SecureDesk provides the following menu:

```text
========== MAIN MENU ==========

1. System Information
2. Network Diagnostics
3. Process Monitor
4. Disk Health
5. Windows Security Events
6. Windows Firewall Status
7. View Scan History
8. Generate HTML Security Report
9. Exit
```

---

## Testing

Automated module testing is included in:

```text
tests/test_modules.py
```

Run the tests from the project directory:

```powershell
python tests\test_modules.py
```

Current tests verify:

```text
=======================================================
       SECUREDESK MODULE TESTING
=======================================================
PASS: System Information
PASS: Network Diagnostics
PASS: Process Monitor
PASS: Disk Health
PASS: Security Events
PASS: Firewall Check

=======================================================
ALL TESTS COMPLETED SUCCESSFULLY
=======================================================
```

All current module tests completed successfully during development.

---

## Security Considerations

SecureDesk is a monitoring and diagnostic tool.

It does not claim to provide complete endpoint protection, antivirus functionality, or enterprise-grade SIEM capabilities.

The following results should be treated as indicators for further investigation:

- High CPU usage
- High memory usage
- Unfamiliar processes
- Multiple failed login attempts
- Disabled firewall profiles
- Network connectivity failures
- High disk usage

A detected condition does not by itself prove that a security incident or malicious activity has occurred.

---

## Limitations

The current version has the following limitations:

- Windows-focused implementation
- Basic rule-based security analysis
- No real-time continuous monitoring
- No centralized dashboard
- No malware detection engine
- No automated incident response
- Security Event Log results depend on available Windows event records and permissions
- Network diagnostics use basic connectivity tests
- Process monitoring does not determine whether a process is malicious

---

## Future Improvements

Possible future improvements include:

- Real-time endpoint monitoring
- Windows service monitoring
- More detailed Event Log analysis
- Suspicious process detection rules
- Configurable security thresholds
- Email security alerts
- JSON report generation
- Graphical user interface
- Advanced security dashboard
- Scheduled scans
- Additional Windows Event IDs
- Network adapter and gateway information
- Integration with threat intelligence services
- Expanded automated testing

---

## Learning Outcomes

This project demonstrates practical experience with:

- Python programming
- Python modules
- Exception handling
- Windows administration
- PowerShell integration
- Process monitoring
- Network diagnostics
- Windows Security Event Logs
- Security event analysis
- Firewall monitoring
- SQLite databases
- Application logging
- HTML report generation
- Automated testing
- Basic cybersecurity monitoring concepts

---

## Disclaimer

SecureDesk is an educational cybersecurity and IT-support portfolio project.

It is intended for authorized system monitoring, troubleshooting, and learning purposes.

The project should only be used on systems that you own or have permission to monitor.

---

## Author

**Madhura Jambe**

BSc Cyber Security Student

Cybersecurity | Python | IT Support | Endpoint Security