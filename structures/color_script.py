# cd /Users/wilke/Dropbox/projects/reviews_and_commentaries/AmongSiteRateVariation/figures/nrgReviewData/structures/


def apply_color(pdb, data):
    print pdb, data
    cmd.load("%s.pse"%pdb)
    if data == "WCN":
        max = -2.5
        min = 2.5
    elif data == "rate":
        max = -2.5
        min = 2.5
    else:
        max = 1
        min = 0

    # open the file of new values (just 1 column of numbers, one for each alpha carbon)
    inFile = open("%s-%s.txt" % (pdb, data), 'r')
 
    # create the global, stored array
    stored.newB = []
 
    # read the new B factors from file
    for line in inFile.readlines(): stored.newB.append( float(line) )
 
    # close the input file
    inFile.close()
 
    # clear out the old B Factors
    cmd.alter("%s and n. CA"%pdb, "b=0.0")
 
    # update the B Factors with new properties
    cmd.alter("%s and n. CA"%pdb, "b=stored.newB.pop(0)")
 
    # color the protein based on the new B Factors of the alpha carbons
    cmd.spectrum("b", "rainbow", "%s and n. CA"%pdb, minimum=min, maximum=max)

    cmd.cartoon("tube")

    # set background color
    cmd.bg_color(color="white")
    
    cmd.set( "ray_opaque_background", value=0 )


def make_figure(pdb, data, ray, output):
    apply_color(pdb, data)

    if ray:
        cmd.ray("1200", "900")
    if output:
        cmd.png("%s-%s.png" % (pdb, data) [0:4])


pdb_list = ['1OGO', '1AKO', '1LVH', '1R44']
#pdb_list = ['1R44']

data_list = ['WCN', 'RSA', 'rate']
#data_list = ['rate']

ray = True
output = True

for pdb in pdb_list:
    for data in data_list:
        make_figure(pdb, data, ray, output)

