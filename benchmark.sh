#!/bash/bin
# Stress test script for Compute-as-a-Service

echo "Testing Baseline (No Latency)..."
python3 client.py

echo "---"
echo "Simulating 5G Network (10ms delay)..."
sudo tc qdisc add dev lo root netem delay 10ms
python3 client.py
sudo tc qdisc del dev lo root

echo "---"
echo "Simulating Poor Network (200ms delay, 5% loss)..."
sudo tc qdisc add dev lo root netem delay 200ms loss 5%
python3 client.py
sudo tc qdisc del dev lo root