read -p "Introduce un numero: " num

if ((num < 2)); then
    echo "No es primo"
    exit 0
fi

for ((i = 2; i*i <= num; i++)); do
    if ((num % i == 0)); then
        echo "No es primo"
        exit 0
    fi
done

echo "Es primo"