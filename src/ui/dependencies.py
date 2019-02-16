"""
Dépendances du package ui.
"""

import os
from collections import *
from datetime import *
from typing import *

Photo = namedtuple('Photo', 'path date place classifications')

def getPhotos(sort: str, order: str) -> List[Photo]:
    """
    Retourne l'ensemble des photos de l'utilisateur.

    @param sort: Ordre de tri des photos.
                 Valeurs possibles : "date", "place", "people", "classifications".
    @param order: Indique si le tri doit se faire en ordre croisssant (asc), ou décroissant (desc).

    @return: Liste des photos triées de l'utilisateur.
    """
    imagesDirectory = os.path.join('res', 'images', 'samples')
    return [Photo(os.path.join(imagesDirectory, imageName), None, None, []) for imageName in sorted(os.listdir(imagesDirectory))] * 10
