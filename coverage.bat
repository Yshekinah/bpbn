C:
cd C:\Users\David\Domainmanager_virtualenv\Scripts
activate.bat
coverage.exe run --omit="D:\Stuff\Django_projects\bpbn_github\bpbn\domainmanager\migrations\*","C:\Users\David\Domainmanager_virtualenv\*" D:\Stuff\Django_projects\bpbn_github\bpbn\manage.py test -v 2
coverage.exe html