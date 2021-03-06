# -*- coding: utf-8 -*-
#
#    Copyright 2009, 2010, 2011, 2012 Sébastien Bonnegent
#
#    This file is part of POSSUM.
#
#    POSSUM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    POSSUM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with POSSUM.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import models
import logging
#import io

from django.conf import settings
from possum.base.stats import StatsJour, StatsJourGeneral, \
    StatsJourPaiement, StatsJourProduit, StatsJourCategorie
from possum.base.bill import Facture, Suivi
from possum.base.generic import Nom, NomDouble, Priorite, Etat
from possum.base.log import LogType, Log
from possum.base.product import Produit, ProduitVendu
from possum.base.payment import PaiementType, Paiement
from possum.base.color import Couleur
from possum.base.category import Categorie
from possum.base.options import Cuisson, Sauce, Accompagnement
from possum.base.location import Zone, Table



