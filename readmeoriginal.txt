dlib インストール方法

python3
brew install boost
brew install boost-python --with-python3
brew install cmake
brew install opencv
pip3 install --upgrade setuptools
pip3 install opencv-python
pip3 install scikit-image
pip3 install dlib
git clone -b v19.0 --depth=1 https://github.com/davisking/dlib
cd dlib/tools/imglab/ && mkdir build && cd build && cmake .. && cmake --build . --config Release
sudo make install

ビルドに失敗したら
https://www.xquartz.org/
からXQuartzというソフトウェアをダウンロードしてインストールする。
 export CPPFLAGS=-I/opt/X11/include
ln -s /opt/X11/include/X11 /usr/local/include/X11

CmakeCache.txt の編集
dlib-19.13/tools/imglab/build/CMakeCache.txt
の
DLIB_NO_GUI_SUPPORT:STRING=OFF
の OFF を ON に変更します

使い方
example1stをコピー
learning に学習用の画像を入れる(jpg)
learning で必要なファイルを作成
imglab -c mydataset.xml .
画像の読み取り範囲を指定するコマンド
imglab mydataset.xml
学習を実行
python3 train_object_detector.py learning
テスト検出
python3 detect_object_detector.py test
