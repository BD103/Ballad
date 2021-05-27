import subprocess


def install(dependency: str):
  print("Installing:", dependency)
  subprocess.run(["python", "-m", "pip", "install", "-qq", dependency])
