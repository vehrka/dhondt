#!/usr/bin/env python3
# −*− coding: UTF−8 −*−


class dhondt():
    """Class to calculate d'Hondt statistics

    The minimum data is:

    + The number of seats [nrep]
    + The minimum percentage to get into the calculation [minper]
    + A dictionary with the votes of the candidatures [dcandi]
         dcandi = {'000001': 51000, '000002': 46000, '000007': 34000, '000006': 29000, 'others': 31000}

    CAVEAT LECTOR
    + It doesn't resolve seat ties
    + Always gets rid of a party called 'others'
    """
    def __init__(self, nrep, minper, dcandi, census=0, vwhite=0, vnull=0):
        self.nrep = nrep
        self.minper = minper
        self.census = census
        self.vwhite = vwhite
        self.vnull = vnull
        self.dcandi = dcandi.copy()
        self.calc()

    def __repr__(self):
        candidatures = sorted(self.dcandi.items(), key=lambda p: p[1], reverse=True)
        return '<dhondt nrep:{0} minper:{1} candi:{2}>'.format(self.nrep, self.minper, candidatures)

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
        # TODO: Finish script with the RESULTS and PARTICIPATION sections
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

        # Prepare the lists for the calculations
        candinames = [p[0] for p in candivali]
        candimaxis = [p[1] for p in candivali]
        canditrab = [(p[1], 0) for p in candivali]

        # Prepare the dictionaries for the results
        self.repre = dict(zip(candinames, [0 for name in candinames]))
        self.asigna = dict(zip(candinames, [[maxi] for maxi in candimaxis]))

        # Perform the seat calculation
        for i in range(self.nrep):
            # Find the party with the maximum nunber of votes in this round
            dic01 = dict(zip(candinames, canditrab))
            odic01 = sorted(dic01.items(), key=lambda p: p[1][0], reverse=True)
            parmax = odic01[0][0]
            inparmax = candinames.index(parmax)
            maxivotos = candimaxis[inparmax]
            nrepre = canditrab[inparmax][1]
            # This line does the magic
            canditrab[inparmax] = (maxivotos / (nrepre + 2), nrepre + 1)
            self.repre[parmax] = nrepre + 1
            # Fill the asignation table dictionary
            for j, trab in enumerate(canditrab):
                self.asigna[candinames[j]].append(int(trab[0]))
            # We need to know which was the party assigned with the seat before the last seat
            if i == self.nrep - 2:
                penparmax = parmax

        # Calculate the votes needed for another seat
        self.falta = {}
        votult = self.asigna[parmax][-2]

        for name in candinames:
            votu = self.dcandi[name]
            crep = self.repre[name]
            if name == parmax:
                # The last asigned seat gets the number differently
                crepp = self.repre[penparmax]
                votp = self.dcandi[penparmax]
                vfalta = int(votp / crepp * (crep + 1) - votu)
            else:
                cvot = self.asigna[name][-1]
                vfalta = int((votult - cvot) * (crep + 1))
            pfalta = (vfalta / votu) * 100.0
            # Stores the number of votes and the percentage over the actual votes
            self.falta[name] = (vfalta, pfalta)


if __name__ == '__main__':
    """Performs the d'hondt calculation"""
    # TODO: Add argument parser
    # Gets the input data
    ## nrep, minper, census, white, vnull, nabs, dcandi
    # Performs the dhont calc
    # Returns data calc
