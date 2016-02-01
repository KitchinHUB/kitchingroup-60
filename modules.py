import os

def getvdw(path):
    files = os.listdir(path)
    filename = path.split('/')[-1]

    for f in files:
        if filename in f:
            with open(path+'/'+f) as f:
                content = f.readlines()
                for text in reversed(content):
                    if 'Total vdW correction in eV:' in text:
                        _, vdw_corr = text.split(':')
                        return float(vdw_corr)
                        break
                    else:
                        pass
        else:
            pass
