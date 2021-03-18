#/bin/sh

find ../examples/ -name '*.ipynb' | while read f; do
    if [[ $f != *".ipynb_checkpoints"* ]]; then
        echo $f
        python scripts/ipynb_to_gallery.py $f
    fi 
done