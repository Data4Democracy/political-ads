import fcc

#Facility(id=1051)#.fetch()

print([facility.metadata for facility in fcc.Facility.getAll(fetchMetaData=True, save=True)])