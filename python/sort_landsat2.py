#!/usr/bin/env python

import gdal # Import GDAL library bindings
import os
import sys
sys.path.insert(0,'python')
from gdal_merge import main as gdal_merge
from spectral import *
import spectral.io.envi as envi

def tiff2envi(ofile):

  # loop over _refl and _mask file
  for o in [ofile + '_refl.tif',ofile + '_mask.tif']:
    # open tiff file
    dataset = gdal.Open(o, GA_ReadOnly)
    # read the tiff data
    data = dataset.ReadAsArray()

    # set up metadata for envi file

    md = {'lines': dataset.RasterYSize,
          'samples': dataset.RasterXSize,
          'bands': dataset.RasterCount}
    # save envi file

    envi.save_image(o.replace('tif','hdr'),data,metadata=md,\
                        dtype='float32',interleave='bip',force=True)



def rm(x):
    for f in x:
        try:
            os.remove(f)
        except:
            pass

# pull out only the reflectance bands
def sort_landsat(files):
  ofiles = []
  for d in files:
    bfiles = []
    for f in d:
        try:
            f.index('_sr_band')
            bfiles.append(f)
        except:
            pass
    try:
        # output file name
        ofile = bfiles[0].split('_sr_band')[-2].split('/')[-1]
        ofile1 = ofile + '_mask'
        ofile2 = ofile + '_refl.tif'
        ofile3 = ofile + '_mask.tif'
        ofiles = [ofile,ofile1,ofile2,ofile3]
        mfile = bfiles[0].split('_sr_band')[-2] + '_cfmask.tif'
        rm(ofiles)
        
        # build a command line to run
        box = "-ul_lr 767385 2533665 827985 2493765"
        box = ""
        nbfiles = []
        
        # loop over the band files
        # and apply scale
        for b in bfiles:
            # now multiply by 0.001
            bfiles2 = b + '_tmp'
            rm([bfiles2])
            # bug means need to do it twice here
            cmd = "python/gdal_calc.py --type=Float32 -A " + b + \
              ' --outfile=' + bfiles2 + ' ' + bfiles2 + \
                ' --calc="A*0.001"'
            os.system(cmd)
            nbfiles.append(bfiles2)
        # delete the original band files
        rm(bfiles)
        
        # 
        cmd = 'gdal_merge -o ' + ofile2 + ' ' + \
             ' '.join(nbfiles) + ' -separate -ot Float32 -v ' + box 
        gdal_merge(cmd.split())
        # mask 
        cmd = 'gdal_merge -o ' + ofile1 + ' ' + \
             mfile + ' -separate -ot Float32 -v ' + box 
        gdal_merge(cmd.split())
        # mask create
        cmd = "python/gdal_calc.py -A " + ofile1 + \
              ' --outfile=' + ofile3 + ' --calc="~((A == 1) + (A == 0))"'
        os.system(cmd)
        
        # convert to envi
        tiff2envi(ofile)
        
        # tidy up
        rm([ofile2,ofile3])
        rm([ofile,ofile1])
        rm(nbfiles)
        ofiles.append([ofile2,ofile3])
    except:
        pass
  return ofiles
