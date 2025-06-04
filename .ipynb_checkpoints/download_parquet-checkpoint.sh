cd parquet_data
while read url; do
  filename=$(basename "$url")
  if [ -f "$filename" ]; then
    echo "Skipping $filename (already exists)"
  else
    echo "Downloading $filename"
    wget "$url"
  fi
done < paths.txt
