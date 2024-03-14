import os
import subprocess


class CertificadosManager:
    def __init__(self) -> None:
        self.password = os.environ.get("CERTIFICADOS_PASS")
        self.certificados_path = os.environ.get("CERTIFICADOS_PATH")
        # lpszStoreProvider
        self.CERT_STORE_PROV_SYSTEM = 0x0000000A

        # dwFlags
        self.CERT_SYSTEM_STORE_LOCAL_MACHINE = 0x00020000

    def install_certificado(self, pfx_path):
        """
        Instala um certificado PFX no armazenamento de certificados "MY" no contexto da máquina local
        usando a ferramenta de linha de comando certutil.
        """
        # Constrói o comando para importar o certificado PFX
        command = f'certutil -f -p "{self.password}" -importPFX -user "{pfx_path}"'

        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Certificado '{pfx_path}' instalado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar o certificado '{pfx_path}': {e}")

    def scan_and_install_certificates(self):
        for root, dirs, files in os.walk(self.certificados_path):
            for file in files:
                if file.endswith(".pfx"):
                    pfx_path = os.path.join(root, file)
                    print(f"Enviando para instalar pfx: %s" % pfx_path)
                    self.install_certificado(pfx_path)

    def desinstalar_certificado(self, thumbprint):
        """
        Desinstala um certificado do armazenamento de certificados "MY" no contexto da máquina local
        usando a ferramenta de linha de comando certutil.
        """
        # Constrói o comando para remover o certificado pelo thumbprint
        command = f'certutil -delstore -user "MY" "{thumbprint}"'

        try:
            subprocess.run(command, check=True, shell=True)
            print(
                f"Certificado com thumbprint '{thumbprint}' desinstalado com sucesso."
            )
        except subprocess.CalledProcessError as e:
            print(
                f"Erro ao desinstalar o certificado com thumbprint '{thumbprint}': {e}"
            )

    def desinstalar_todos_ceriticados(self):
        command = f"Get-ChildItem -Path Cert:\CurrentUser\My\ | Remove-Item"

        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Certificados desinstalados com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao desinstalar certificados: {e}")
