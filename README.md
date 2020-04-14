# simplescanner


安装masscna
git clone https://github.com/robertdavidgraham/masscan.git
make regress

安装nmap
git clone https://github.com/nmap/nmap
./configure
make
make install

通过masscan的快速扫描获取目标IP端口，提取后交由nmap扫描。
目前实现单个ip扫描