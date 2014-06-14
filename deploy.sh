orchard docker kill $(orchard docker ps -q)
cd backend && orchard docker build -t backend .
cd ..
orchard docker run -d -p 8000:8000 -t backend
cd frontend && orchard docker build -t frontend .
cd ..
echo 'starting docker'
orchard docker run -d -p 80:80 -t frontend
