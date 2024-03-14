import os, logging
from infrastructure import SharePoint
from domain import SharepointSettings
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    config = SharepointSettings(
        site_url=os.getenv("SP_SITE_URL"),
        site_path=os.getenv("SP_SITE_PATH"),
        tenant_id=os.getenv("SP_TENANT_ID"),
        client_id=os.getenv("SP_CLIENT_ID"),
        client_secret=os.getenv("SP_CLIENT_SECRET"),
    )

    sp = SharePoint(config)
    file_path = os.environ.get("SP_FILE_PATH")
    folder_path = "Certiões"
    local_save_path = os.environ.get("SP_LOCAL_SAVE_PATH")

    try:
        sp.list_folders_in_root()
        # sp.upload_file_to_sharepoint(file_path, folder_path)
        # sp.download_file_from_sharepoint(file_path, local_save_path)
    except Exception as e:
        logging.error(e)
