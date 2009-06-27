# -*- coding: utf-8 -*-
# Last Change: Wed Jun 24 06:00 PM 2009 J

# The code and descriptive text is copyrighted and offered under the terms of
# the BSD License from the authors; see below. However, the actual dataset may
# have a different origin and intellectual property status. See the SOURCE and
# COPYRIGHT variables for this information.

# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     * Neither the author nor the names of any contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Star98 Educational Testing dataset."""

__docformat__ = 'restructuredtext'

COPYRIGHT   = """Permission granted by the author"""
TITLE       = "Star98 Educational Dataset"
SOURCE      = """
http://jgill.wustl.edu/research/books.html

Dr. Jeff Gill
Department of Political Science
One Brookings Drive, Seigle L079
Washington University
St. Louis, MO 63130-4899
"""

DESCRSHORT  = """Math scores for 303 student with 10 explanatory factors"""

DESCRLONG   = """
This data is on the California education policy and outcomes (STAR program
results for 1998.  The data measured standardized testing by the California
Department of Education that required evaluation of 2nd - 11th grade students
by the the Stanford 9 test on a variety of subjects.  This dataset is at
the level of the unified school district and consists of 303 cases.  The
binary response variable represents the number of 9th graders scoring
over the national median value on the mathematics exam.

The original source files and information are included in /star98/src/

The data used in this example is only a subset of the original source.

/star98/star98.csv contains this subset and interaction variables
in a comma-delimited file
"""

NOTE        = """
Number of Instances: 303. 145 for MATHNCE9 > 50 (above national median)
and 158 for MATHNCE9 < 50 (below median).

Number of Attributes: 12 and 8 interaction terms.

label: 0 for below median, 1 for above median

Missing Attribute Values: None
"""

class load():
    """load the star98 data and returns them.

    :returns:
        data instance:
            a class of the data with array attrbutes 'endog' and 'exog'
    """
#    from star98 import outcome, lowinc, perblack, perhisp, avyrsexp, avsal,\
#        ptratio, pctaf, pctchrt, pctyrrnd, perminte_avyrsexp, perminte_avsal, \
#        avyrsexp_avsal, perspen_ptratio, perspen_pctaf, ptratio_pctaf, \
#        perminte_avyrsexp_avsal, perspen_ptratio_pctaf

#    names = [outcome, lowinc, perblack, perhisp, avyrsexp, avsal,
#        ptratio, pctaf, pctchrt, pctyrrnd, perminte_avyrsexp, perminte_avsal,
#        avyrsexp_avsal, perspen_ptratio, perspen_pctaf, ptratio_pctaf,
#        perminte_avyrsexp_avsal, perspen_ptratio_pctaf]

    _endog = None
    _exog = None
    def __init__(self):
        import numpy as np
        from star98 import __dict__, names
        self._names = names
        self._d = __dict__

#    def __call__(self):
#        self.regressor = 'outcome'      # define the model above and scrape
                                            # for this so it's reusable
                                        # or just order the data correctly...
#        self._d = __dict__
#        names = d.keys()
#        names.sort
#        while names[0].startswith('_'): names.remove(names[0])
#        self._names = names
 #       endog = np.array(d[names['outcome'])
 #       for i in range(len):

    @property
    def endog(self):
        if self._endog is None:
            self.endog = np.array(self._d[self._names[0]], dtype=np.float)
        return self.endog

    @property
    def exog(self):
        if self._exog is None:
            self.exog = np.column_stack(self._d[i] \
                    for i in self._names[1:]).astype(np.float)
        return self.exog
#    for i in range(len(names)):
#        names[i] = np.array(names[i]).astype(np.float)[:,None]

#    outcome = np.array(outcome).astype(np.float)
#    lowinc = np.array(lowinc).astype(np.float)
#    perblack = np.array(perblack).astype(np.float)
#    perhisp = np.array(perhisp).astype(np.float)
#    avrysexp = np.array(avrysexp).astype(np.float)
#    avsal = np.array(avsal).astype(np.float)
#    ptratio = np.array(ptratio).astype(np.float)
#    pctaf = np.array(pctaf).astype(np.float)
#    pctyrrnd = np.array(pctyrrnd).astype(np.float)
#    perminte_avrysexp = np.array(perminte).astype(np.float)
#    avrysexp_avsal = np.array(avrysexp_avsal).astype(np.float)
#    perspen_ptratio = np.array(perspen_ptratio).astype(np.float)
#    perspen_pctaf = np.array(perspen_pctaf).astype(np.float)
#    ptratio_pctaf = np.array(ptratio_pctaf).astpye(np.float)
#    perminte_avyrsexp_avsal = np.array(perminte_avrysexp_avsal).\
#            astype(np.float)
#    perspen_ptratio_pctaf = np.array(perspen_ptratio_pctaf)

#    exog = zip((names[i][1:))
#    d = zip(names[0],exog)
#    data = np.array((names[0],exog))
#    dt = np.dtype([('endog',np.float),('exog', np.array, (1, 5))])
#    data = data.view(np.recarray, dtype=dt)
# this could return y,x or endog, exog...
#    return data
