import time
import psutil
import pynvml
import runpod

# ---------------------
# INIT
# ---------------------
pynvml.nvmlInit()

MAX_GPU_UTIL = 85       # Prozent
MAX_CPU_UTIL = 85       # Prozent
CHECK_INTERVAL = 0.2    # Sekunden


def wait_for_safe_usage():
    """Wartet, bis CPU und GPU unter 85 % liegen."""
    while True:
        # CPU-Abfrage
        cpu_util = psutil.cpu_percent(interval=0.1)

        # GPU-Abfrage
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            gpu_util = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        except:
            gpu_util = 0   # falls kein Zugriff

        if cpu_util < MAX_CPU_UTIL and gpu_util < MAX_GPU_UTIL:
            break  # alles im grünen Bereich

        time.sleep(CHECK_INTERVAL)


def run_job(job):
    """Hier wird deine eigentliche Aufgabe ausgeführt."""

    wait_for_safe_usage()  # sorgt für 85%-Limit

    # Beispielaufgabe — nur Test:
    result = {
        "cpu_util": psutil.cpu_percent(),
        "message": "Task completed safely under 85% load."
    }

    return result


runpod.serverless.start({
    "handler": run_job
})
