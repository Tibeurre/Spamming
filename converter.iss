[Setup]
AppName=Farfadet Malicieux
AppVersion=1.0
DefaultDirName={pf}\FarfadetMalicieux
DefaultGroupName=FarfadetMalicieux
OutputDir=.
OutputBaseFilename=FarfadetInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\FarfadetMalicieux\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Farfadet Malicieux"; Filename: "{app}\FarfadetMalicieux.exe"
