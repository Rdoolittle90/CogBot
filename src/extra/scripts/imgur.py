from imgurpython import ImgurClient
from os import getenv


client = ImgurClient(getenv("IMGUR_CLIENT_ID"), getenv("IMGUR_CLIENT_SECRET"))


def upload_image_to_imgur(path):
    """Upload an image to Imgur and return its direct link."""
    image = client.upload_from_path(path)
    return image['link']


if __name__ == "__main__":
    image_url = upload_image_to_imgur("src/save/temp/sc/165453570227961856_Profit_Chart.png")
    print(image_url)