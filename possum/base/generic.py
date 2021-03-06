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

LONGUEUR_FACTURE = 35
LONGUEUR_IHM = 60

# les classes generiques
class Nom(models.Model):
    nom = models.CharField(max_length=LONGUEUR_IHM)

    def __unicode__(self):
        return self.nom

    def __cmp__(self,other):
        return cmp(self.nom, other.nom)

    class Meta:
        abstract = True
        ordering = ['nom']

class NomDouble(Nom):
    nom_facture = models.CharField(max_length=LONGUEUR_FACTURE)

    class Meta:
        abstract = True

class Priorite(models.Model):
    """Getter / setter: si priorite inferieur à 0 on reste à 0
    """
    priorite = models.PositiveIntegerField(default=0)


    class Meta:
        abstract = True
        ordering = ['priorite']

    def __cmp__(self, other):
        return cmp(self.priorite,other.priorite)

class Etat(Nom, Priorite):
    """Etat d'une facture"""

    def __cmp__(self, other):
        return cmp(self.priorite,other.priorite)

