import sys

def filter_xml (infile, outfile):
    import re
    out_string = ''
    with open(infile) as instream:
        instring = instream.read()
        xml_pattern = re.compile('<[^>]*>')
        out_string = re.sub(xml_pattern,'',instring)
        amp_pattern=re.compile('&[^;]*;')
        oout_string=re.sub(amp_pattern,'',out_string)
    with open(outfile,'w') as outstream:
        outstream.write(oout_string)

def main(args):
    infile = args[1]
    split_point = infile.rindex('.')
    outfile = infile[:split_point]+'.txt'
    filter_xml(infile,outfile)

sys.exit(main(sys.argv))

