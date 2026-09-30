import os
import webbrowser
from datetime import datetime


REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(
    REPORT_FOLDER,
    "securedesk_report.html"
)


def generate_recommendations(
    system_data,
    network_data,
    disk_data,
    security_data,
    firewall_data
):

    recommendations = []

    # Disk recommendations
    if disk_data["status"] == "CRITICAL":

        recommendations.append(
            "CRITICAL: Disk usage is extremely high. "
            "Free up storage space and investigate large files."
        )

    elif disk_data["status"] == "WARNING":

        recommendations.append(
            "WARNING: Disk usage is high. "
            "Consider removing unnecessary files."
        )

    else:

        recommendations.append(
            "PASS: Disk usage is within the configured "
            "normal range."
        )


    # Network recommendations
    if network_data["internet"] != "PASS":

        recommendations.append(
            "WARNING: Internet connectivity check failed. "
            "Check the network connection."
        )

    else:

        recommendations.append(
            "PASS: Internet connectivity is available."
        )


    if network_data["dns"] != "PASS":

        recommendations.append(
            "WARNING: DNS resolution failed. "
            "Check DNS configuration and network settings."
        )

    else:

        recommendations.append(
            "PASS: DNS resolution is working."
        )


    # Security event recommendations
    if security_data["failed_logins"] >= security_data["threshold"]:

        recommendations.append(
            "WARNING: Multiple failed login attempts were "
            "detected. Review Windows Security Events "
            "and investigate the source."
        )

    else:

        recommendations.append(
            "PASS: No unusual number of failed login "
            "attempts was detected during the analysis period."
        )


    # Firewall recommendations
    if firewall_data["status"] == "WARNING":

        recommendations.append(
            "WARNING: One or more Windows Firewall profiles "
            "are disabled. Review firewall configuration."
        )

    elif firewall_data["status"] == "PASS":

        recommendations.append(
            "PASS: All detected Windows Firewall profiles "
            "are enabled."
        )

    else:

        recommendations.append(
            "WARNING: Windows Firewall status could not "
            "be completely verified."
        )


    # CPU recommendation
    if system_data["cpu_usage"] >= 90:

        recommendations.append(
            "WARNING: CPU usage is very high. "
            "Review resource-intensive processes."
        )

    else:

        recommendations.append(
            "PASS: CPU usage is below the high-usage threshold."
        )


    # Memory recommendation
    if system_data["memory_usage"] >= 90:

        recommendations.append(
            "WARNING: Memory usage is very high. "
            "Review running applications and processes."
        )

    else:

        recommendations.append(
            "PASS: Memory usage is below the high-usage threshold."
        )


    return recommendations


def generate_html_report(
    system_data,
    network_data,
    disk_data,
    security_data,
    firewall_data,
    scan_history
):

    os.makedirs(
        REPORT_FOLDER,
        exist_ok=True
    )

    generated_time = datetime.now().strftime(
        "%d %B %Y, %H:%M:%S"
    )


    # Generate recommendations
    recommendations = generate_recommendations(
        system_data,
        network_data,
        disk_data,
        security_data,
        firewall_data
    )


    # Firewall table
    firewall_rows = ""

    for profile in firewall_data["profiles"]:

        status = (
            "ENABLED"
            if profile["enabled"]
            else "DISABLED"
        )

        firewall_rows += f"""
        <tr>
            <td>{profile["name"]}</td>
            <td>{status}</td>
        </tr>
        """


    # Scan history table
    history_rows = ""

    for record in scan_history:

        history_rows += f"""
        <tr>
            <td>{record[0]}</td>
            <td>{record[1]}</td>
            <td>{record[2]}</td>
            <td>{record[3]}</td>
            <td>{record[4]}</td>
        </tr>
        """


    # Recommendation list
    recommendation_rows = ""

    for recommendation in recommendations:

        if recommendation.startswith("WARNING"):

            css_class = "warning"

        elif recommendation.startswith("CRITICAL"):

            css_class = "critical"

        else:

            css_class = "pass"


        recommendation_rows += f"""
        <li class="{css_class}">
            {recommendation}
        </li>
        """


    html = f"""
<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <title>
        SecureDesk Security Report
    </title>


    <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f6f8;
            color: #222;
        }}


        .header {{
            background-color: #1f2937;
            color: white;
            padding: 30px;
            border-radius: 10px;
        }}


        .header h1 {{
            margin-bottom: 5px;
        }}


        h2 {{
            margin-top: 30px;
            border-bottom: 2px solid #ddd;
            padding-bottom: 8px;
        }}


        .card {{
            background-color: white;
            padding: 20px;
            margin-top: 15px;
            border-radius: 8px;
            box-shadow:
                0 2px 6px rgba(0, 0, 0, 0.08);
        }}


        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}


        th,
        td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}


        th {{
            background-color: #e5e7eb;
        }}


        ul {{
            padding-left: 20px;
        }}


        li {{
            margin-bottom: 12px;
            padding: 10px;
            border-radius: 5px;
        }}


        .pass {{
            background-color: #ecfdf5;
            color: #166534;
        }}


        .warning {{
            background-color: #fffbeb;
            color: #92400e;
        }}


        .critical {{
            background-color: #fef2f2;
            color: #991b1b;
        }}


        .footer {{
            margin-top: 40px;
            font-size: 13px;
            color: #666;
        }}

    </style>

</head>


<body>


    <div class="header">

        <h1>
            SECUREDESK
        </h1>

        <p>
            IT Support & Endpoint Security
            Monitoring Report
        </p>

        <p>
            Generated:
            {generated_time}
        </p>

    </div>


    <h2>
        System Information
    </h2>

    <div class="card">

        <p>
            <strong>Hostname:</strong>
            {system_data["hostname"]}
        </p>

        <p>
            <strong>Operating System:</strong>
            {system_data["os"]}
        </p>

        <p>
            <strong>OS Version:</strong>
            {system_data["os_version"]}
        </p>

        <p>
            <strong>Architecture:</strong>
            {system_data["architecture"]}
        </p>

        <p>
            <strong>Processor:</strong>
            {system_data["processor"]}
        </p>

        <p>
            <strong>CPU Usage:</strong>
            {system_data["cpu_usage"]}%
        </p>

        <p>
            <strong>Memory Usage:</strong>
            {system_data["memory_usage"]}%
        </p>

        <p>
            <strong>Disk Usage:</strong>
            {system_data["disk_usage"]}%
        </p>

    </div>


    <h2>
        Network Diagnostics
    </h2>

    <div class="card">

        <p>
            <strong>Hostname:</strong>
            {network_data["hostname"]}
        </p>

        <p>
            <strong>Local IP:</strong>
            {network_data["local_ip"]}
        </p>

        <p>
            <strong>Internet Connectivity:</strong>
            {network_data["internet"]}
        </p>

        <p>
            <strong>DNS Resolution:</strong>
            {network_data["dns"]}
        </p>

    </div>


    <h2>
        Disk Health
    </h2>

    <div class="card">

        <p>
            <strong>Total Space:</strong>
            {disk_data["total_gb"]:.2f} GB
        </p>

        <p>
            <strong>Used Space:</strong>
            {disk_data["used_gb"]:.2f} GB
        </p>

        <p>
            <strong>Free Space:</strong>
            {disk_data["free_gb"]:.2f} GB
        </p>

        <p>
            <strong>Usage:</strong>
            {disk_data["usage_percent"]:.1f}%
        </p>

        <p>
            <strong>Status:</strong>
            {disk_data["status"]}
        </p>

        <p>
            <strong>Message:</strong>
            {disk_data["message"]}
        </p>

    </div>


    <h2>
        Windows Security Events
    </h2>

    <div class="card">

        <p>
            <strong>Analysis Period:</strong>
            Last 24 hours
        </p>

        <p>
            <strong>Successful Logins (4624):</strong>
            {security_data["successful_logins"]}
        </p>

        <p>
            <strong>Failed Logins (4625):</strong>
            {security_data["failed_logins"]}
        </p>

        <p>
            <strong>Threshold:</strong>
            {security_data["threshold"]}
        </p>

        <p>
            <strong>Status:</strong>
            {security_data["status"]}
        </p>

        <p>
            <strong>Message:</strong>
            {security_data["message"]}
        </p>

    </div>


    <h2>
        Windows Firewall
    </h2>

    <div class="card">

        <p>
            <strong>Overall Status:</strong>
            {firewall_data["status"]}
        </p>

        <p>
            {firewall_data["message"]}
        </p>


        <table>

            <tr>

                <th>
                    Firewall Profile
                </th>

                <th>
                    Status
                </th>

            </tr>

            {firewall_rows}

        </table>

    </div>


    <h2>
        Security Recommendations
    </h2>

    <div class="card">

        <ul>

            {recommendation_rows}

        </ul>

    </div>


    <h2>
        Scan History
    </h2>

    <div class="card">

        <table>

            <tr>

                <th>
                    ID
                </th>

                <th>
                    Scan Type
                </th>

                <th>
                    Status
                </th>

                <th>
                    Details
                </th>

                <th>
                    Timestamp
                </th>

            </tr>

            {history_rows}

        </table>

    </div>


    <div class="footer">

        <p>
            SecureDesk - Python-Based IT Support
            & Endpoint Security Monitoring System
        </p>

        <p>
            This report is generated for monitoring
            and educational purposes.
        </p>

    </div>


</body>

</html>
"""


    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)


    return REPORT_FILE


def open_report():

    report_path = os.path.abspath(
        REPORT_FILE
    )

    if os.path.exists(report_path):

        webbrowser.open(
            "file:///"
            + report_path.replace("\\", "/")
        )

        return report_path

    return None