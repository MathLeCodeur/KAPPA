"""
Dépendances du package ui.
"""

from collections import namedtuple
from datetime import datetime
import os
from typing import List

# Photo et ses données associées.
Photo = namedtuple('Photo', 'path date place classifications')

def get_photos(sort: str, order: str) -> List[Photo]:
    """
    Retourne l'ensemble des photos de l'utilisateur.

    @param sort: Ordre de tri des photos.
                 Valeurs possibles : "date", "place", "people", "classifications".
    @param order: Indique si le tri doit se faire en ordre décroissant (asc),
                  ou décroissant (desc).
    @return: Liste des photos triées de l'utilisateur.
    """
    images_directory = os.path.join('res', 'images', 'samples')
    return [Photo(os.path.join(images_directory, image_name), None, None, []) for image_name in sorted(os.listdir(images_directory))] * 10
