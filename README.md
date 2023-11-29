# health-check
Scripts that check the health of my computers:
1. all_checks_early_exercise.py: A script from an early exercise. Checks local disk/root full, pending reboot, cpu constrained, no network.
   - If pass, prints "Everything ok.". Otherwise, prints error message.
3. health_check_send_email.py: Course end chapter script. Checks cpu constrained, disk full, RAM & localhost ("127.0.0.1").
   - If pass, for each check, print "<system>: OK".
   - If fail, prints error message and sends email:
     - subject: error message
     - body: "Please check your system and resolve the issue as soon as possible."
