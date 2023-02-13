import os
ENV = {
  "HALO_WORK_DIR": "/home/runner/Halo-Next/.halo2",
  "HALO_EXTERNAL_URL": "https://halo-next.vmtask.repl.co",
  "HALO_SECURITY_INITIALIZER_SUPERADMINPASSWORD": "superadmin"
}
for k in ENV:
  os.environ[k]=ENV[k]

filename = open("jarfile.txt","r")
execcommand = "java -jar "+filename.read()
os.system(execcommand)