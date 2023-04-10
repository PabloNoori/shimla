import subprocess
from django import template

register = template.Library()

@register.filter
def check_online(user):

    process = subprocess.run(["sudo", "lsof", "-i", "-n", "-P"], capture_output=True, text=True)
    output = process.stdout

    process = subprocess.run(["grep", "ssh"], input=output, capture_output=True, text=True)
    output = process.stdout

    process = subprocess.run(["grep", user], input=output, capture_output=True, text=True)
    output = process.stdout

    if output:
        return True
    else:
        return False