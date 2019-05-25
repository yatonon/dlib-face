dlib インストール方法

python3
brew install boost
brew install boost-python --with-python3
(brew install boost-python3)
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




                              dlib C++ library

Dlib is a modern C++ toolkit containing machine learning algorithms and tools
for creating complex software in C++ to solve real world problems.  See
http://dlib.net for the main project documentation and API reference.



COMPILING DLIB C++ EXAMPLE PROGRAMS
   Go into the examples folder and type:
       mkdir build; cd build; cmake .. ; cmake --build .
   That will build all the examples.  If you have a CPU that supports AVX
   instructions then turn them on like this:
       mkdir build; cd build; cmake .. -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
   Doing so will make some things run faster.

COMPILING DLIB Python API
   Before you can run the Python example programs you must compile dlib. Type:
       python setup.py install
   or type
       python setup.py install --yes USE_AVX_INSTRUCTIONS
   if you have a CPU that supports AVX instructions, since this makes some
   things run faster.

RUNNING THE UNIT TEST SUITE
   Type the following to compile and run the dlib unit test suite:
       cd dlib/test
       mkdir build
       cd build
       cmake ..
       cmake --build . --config Release
       ./dtest --runall

   Note that on windows your compiler might put the test executable in a
   subfolder called Release.  If that's the case then you have to go to that
   folder before running the test.

This library is licensed under the Boost Software License, which can be found
in dlib/LICENSE.txt.  The long and short of the license is that you can use
dlib however you like, even in closed source commercial software.

Dlib Sponsors:
  This research is based in part upon work supported by the Office of the
  Director of National Intelligence (ODNI), Intelligence Advanced Research
  Projects Activity (IARPA) under contract number 2014-14071600010. The
  views and conclusions contained herein are those of the authors and
  should not be interpreted as necessarily representing the official policies
  or endorsements, either expressed or implied, of ODNI, IARPA, or the U.S.
  Government.
