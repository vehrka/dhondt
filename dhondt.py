#!/usr/bin/env python3
# −*− coding: UTF−8 −*−


class dhondt():
    """Class to calculate d'Hondt statistics

    doesn't resolve ties
    gets rid of a party called 'others'
    """
    def __init__(self, nrep, minper, dcandi, census=0, vwhite=0, vnull=0):
        self.nrep = nrep
        self.minper = minper
        self.census = census
        self.vwhite = vwhite
        self.vnull = vnull
        self.dcandi = dcandi.copy()

    #### TODO: check the datatypes and changes nulls for 0
    @property
    def nrep(self):
        return self.__nrep

    @nrep.setter
    def nrep(self, nrep):
        # TODO: Check is a number and > 0
        self.__nrep = nrep

    @property
    def minper(self):
        return self.__minper

    @minper.setter
    def minper(self, minper):
        # TODO: Check is a number and > 0
        self.__minper = minper

    @property
    def census(self):
        return self.__census

    @census.setter
    def census(self, census):
        # TODO: Check is a number and > 0 or set 0
        self.__census = census

    @property
    def vwhite(self):
        return self.__vwhite

    @vwhite.setter
    def vwhite(self, vwhite):
        # TODO: Check is a number and > 0 or set 0
        self.__vwhite = vwhite

    @property
    def vnull(self):
        return self.__vnull

    @vnull.setter
    def vnull(self, vnull):
        # TODO: Check is a number and > 0 or set 0
        self.__vnull = vnull

    @property
    def dcandi(self):
        return self.__dcandi

    @dcandi.setter
    def dcandi(self, dcandi):
        if type(dcandi) is dict:
            self.__dcandi = dcandi.copy()
            # TODO: Check candidatures names not null and votes are numeric and not null
        else:
            raise AttributeError('dcandi must be a dictionary')

    def calc(self):
        """Performs the calculation"""
        # TODO: Check for data setting
        vtot = sum(self.dcandi.values())
        #ncan = len(self.dcandi)
        #if self.census < (vtot + self.vwhite + self.vnull):
            #bvcensus = False
            #self.census = 0
            #nabs = 0
        #else:
            #bvcensus = True
            #nabs = self.census - vtot - self.vwhite - self.vnull
        # Sort the candidatures in descending number of votes
        candidatures = sorted(self.dcandi.items(), key=lambda p: p[1], reverse=True)
        minvot = ((vtot * self.minper) / 100) - 1
        # Filter the candidatures that have not reached the minimum
        candismin = list(filter(lambda p: p[1] > minvot, candidatures))
        candivali = list(filter(lambda p: p[0] != 'other', candismin))
        #candirest = list(filter(lambda p: p[1] < minvot + 1, candidatures))

        candinames = [p[0] for p in candivali]
        candimaxis = [p[1] for p in candivali]
        canditrab = [(p[1], 0) for p in candivali]

        self.repre = dict(zip(candinames, [0 for name in candinames]))
        self.asigna = dict(zip(candinames, [[maxi] for maxi in candimaxis]))

        for i in range(self.nrep):
            dic01 = dict(zip(candinames, canditrab))
            odic01 = sorted(dic01.items(), key=lambda p: p[1][0], reverse=True)
            parmax = odic01[0][0]
            inparmax = candinames.index(parmax)
            maxivotos = candimaxis[inparmax]
            nrepre = canditrab[inparmax][1]
            canditrab[inparmax] = (maxivotos / (nrepre + 2), nrepre + 1)
            self.repre[parmax] = nrepre + 1
            for j, trab in enumerate(canditrab):
                self.asigna[candinames[j]].append(int(trab[0]))
            if i == self.nrep - 2:
                penparmax = parmax

        self.falta = {}
        votult = self.asigna[parmax][-2]

        for name in candinames:
            votu = self.dcandi[name]
            crep = self.repre[name]
            if name == parmax:
                crepp = self.repre[penparmax]
                votp = self.dcandi[penparmax]
                vfalta = int(votp / crepp * (crep + 1) - votu)
            else:
                cvot = self.asigna[name][-1]
                vfalta = int((votult - cvot) * (crep + 1))
            pfalta = (vfalta / votu) * 100.0
            self.falta[name] = (vfalta, pfalta)


if __name__ == '__main__':
    """Performs the d'hondt calculation"""
    # TODO: Add argument parser
    # Gets the input data
    ## nrep, minper, census, white, vnull, nabs, dcandi
    # Performs the dhont calc
    # Returns data calc
