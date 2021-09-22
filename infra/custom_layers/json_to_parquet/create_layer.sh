set -e

LAYER_NAME=json2parquet.zip
ENV_FOLDER=env
LAYER=python

if test -d "$LAYER" ; then
    rm -rf $LAYER
fi

if test -d "$ENV_FOLDER" ; then
    rm -rf $ENV_FOLDER
fi

python3.8 -m venv $ENV_FOLDER
source $ENV_FOLDER/bin/activate

pip install fastparquet==0.7.1

mkdir $LAYER
mv $ENV_FOLDER/lib64/python3.8/site-packages/* $LAYER

cd $LAYER
rm -rf *.dist-info __pycache__ pip easy_install.py
cd ..

zip -r $LAYER_NAME $LAYER
deactivate

rm -rf $ENV_FOLDER $LAYER