python nano.py
modprobe v4l2_common && python demo.py &
cd /data
python -m http.server 80
