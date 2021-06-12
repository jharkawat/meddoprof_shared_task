set -e
for entry in ../../conll_test/*
do
    echo submitting file "$entry"
    #bsub -n 5 -W 04:00 -J $(basename $entry) -R "rusage[mem= 1024, ngpus_excl_p=1]" -o server_log/$(basename $entry).txt python main.py --config $entry
    python standoff2conll.py $entry >  desire_test_conll/$(basename $entry).txt   
done