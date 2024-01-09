# Define the idle time threshold in seconds (e.g., 300 seconds for 5 minutes)
$idle_time = 300

# Get the last input time (idle time) in seconds
$idleTime = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
$idleTime = (Get-Date) - $idleTime

# Checks the systems idle time and logs them off if the threshold is met.
if ($idleTime.TotalSeconds -gt $idle_time) {
    logoff
}
