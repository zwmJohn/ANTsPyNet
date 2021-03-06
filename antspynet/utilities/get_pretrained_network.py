import requests
import tempfile

from os import path

def get_pretrained_network(file_id=None, target_file_name=None):

    """
    Download pretrained network/weights.

    Arguments
    ---------

    file_id string
        One of the permitted file ids or pass "show" to list all
        valid possibilities. Note that most require internet access
        to download.

    target_file_name string
       Optional target filename.

    Returns
    -------
    A filename string

    Example
    -------
    >>> model_file = get_pretrained_network( 'dbpn4x' )
    """

    def switch_networks(argument):
        switcher = {
            "brainAgeGender": "https://ndownloader.figshare.com/files/22179948",
            # "brainAgeGender": "https://ndownloader.figshare.com/files/14394350",
            "brainExtraction": "https://ndownloader.figshare.com/files/13729661",
            "brainSegmentation": "https://ndownloader.figshare.com/files/13900010",
            "brainSegmentationPatchBased": "https://ndownloader.figshare.com/files/14249717",
            "ctHumanLung": "https://ndownloader.figshare.com/files/20005217",
            "dbpn4x": "https://ndownloader.figshare.com/files/13347617",
            "denoising": "https://ndownloader.figshare.com/files/14235296",
            "functionalLungMri": "https://ndownloader.figshare.com/files/13824167",
            "hippMapp3rInitial": "https://ndownloader.figshare.com/files/18068408",
            "hippMapp3rRefine": "https://ndownloader.figshare.com/files/18068411",
            "mriSuperResolution": "https://ndownloader.figshare.com/files/19430123",
            "protonLungMri": "https://ndownloader.figshare.com/files/13606799",
            "wholeTumorSegmentationT2Flair": "https://ndownloader.figshare.com/files/14087045"
        }
        return(switcher.get(argument, "Invalid argument."))

    if file_id == None:
        raise ValueError("Missing file id.")

    valid_list = ("dbpn4x",
                  "brainAgeGender",
                  "brainExtraction",
                  "brainSegmentation",
                  "brainSegmentationPatchBased",
                  "ctHumanLung",
                  "denoising",
                  "functionalLungMri",
                  "hippMapp3rInitial",
                  "hippMapp3rRefine",
                  "mriSuperResolution",
                  "protonLungMri",
                  "wholeTumorSegmentationT2Flair",
                  "show")

    if not file_id in valid_list:
        raise ValueError("No data with the id you passed - try \"show\" to get list of valid ids.")

    if file_id == "show":
       return(valid_list)

    url = switch_networks(file_id)

    if target_file_name == None:
        target_file = tempfile.NamedTemporaryFile(suffix=".h5")
        target_file.close()
        target_file_name = target_file.name

    if not path.exists(target_file_name):
        r = requests.get(url)
        with open(target_file_name, 'wb') as f:
            f.write(r.content)

    return(target_file_name)






