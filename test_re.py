import re

def run_test( string, extractpattern, matchpattern ) :
    
    e = re.sub( extractpattern, r'\1', string )
    m = re.match( matchpattern, e )
    if m:
        m = '1'
    else:
        m = '0'
    print( string+' --('+extractpattern+')--> '+e+' --('+matchpattern+')--> '+m )

run_test( r'MUON', r'.*MU(\S+).*', r'ON' )
run_test( r'MUOFF', r'.*MU(\S+).*', r'ON' )
run_test( r'SISAT/CBL MUON', r'.*SI(\S+).*', r'SAT/CBL' )
run_test( r'SIGAME MUON', r'.*SI(\S+).*', r'SAT/CBL' )

