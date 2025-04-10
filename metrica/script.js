document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('notasForm');
    const corpoTabela = document.getElementById('corpoTabela');
    const totalNota1 = document.getElementById('totalNota1');
    const totalNota2 = document.getElementById('totalNota2');
    const totalNota3 = document.getElementById('totalNota3');
    const mediaTotal = document.getElementById('mediaTotal');
    const notasChart = document.getElementById('notasChart');

    let notas = [];
    let chartInstance = null;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const nome = document.getElementById('nome').value;
        const nota1 = parseFloat(document.getElementById('nota1').value);
        const nota2 = parseFloat(document.getElementById('nota2').value);
        const nota3 = parseFloat(document.getElementById('nota3').value);

        const media = (nota1 + nota2 + nota3) / 3;

        const notaAluno = {
            nome,
            nota1,
            nota2,
            nota3,
            media
        };

        notas.push(notaAluno);
        atualizarTabela();
        calcularTotais();
        atualizarGrafico();
        form.reset();
    });

    function atualizarTabela() {
        corpoTabela.innerHTML = '';
        notas.forEach(nota => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${nota.nome}</td>
                <td>${nota.nota1.toFixed(1)}</td>
                <td>${nota.nota2.toFixed(1)}</td>
                <td>${nota.nota3.toFixed(1)}</td>
                <td>${nota.media.toFixed(1)}</td>
            `;
            corpoTabela.appendChild(tr);
        });
    }

    function calcularTotais() {
        if (notas.length === 0) {
            totalNota1.textContent = '0';
            totalNota2.textContent = '0';
            totalNota3.textContent = '0';
            mediaTotal.textContent = '0';
            return;
        }

        const soma1 = notas.reduce((acc, nota) => acc + nota.nota1, 0);
        const soma2 = notas.reduce((acc, nota) => acc + nota.nota2, 0);
        const soma3 = notas.reduce((acc, nota) => acc + nota.nota3, 0);
        const mediaTotalCalc = notas.reduce((acc, nota) => acc + nota.media, 0) / notas.length;

        totalNota1.textContent = soma1.toFixed(1);
        totalNota2.textContent = soma2.toFixed(1);
        totalNota3.textContent = soma3.toFixed(1);
        mediaTotal.textContent = mediaTotalCalc.toFixed(1);
    }

    function atualizarGrafico() {
        // Destruir o gráfico anterior se existir
        if (chartInstance) {
            chartInstance.destroy();
        }

        // Preparar dados para o gráfico
        const nomes = notas.map(nota => nota.nome);
        const nota1Valores = notas.map(nota => nota.nota1);
        const nota2Valores = notas.map(nota => nota.nota2);
        const nota3Valores = notas.map(nota => nota.nota3);
        const mediaValores = notas.map(nota => nota.media);

        // Criar novo gráfico
        chartInstance = new Chart(notasChart, {
            type: 'bar',
            data: {
                labels: nomes,
                datasets: [
                    {
                        label: 'Curtidas',
                        data: nota1Valores,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)'
                    },
                    {
                        label: 'Comentarios',
                        data: nota2Valores,
                        backgroundColor: 'rgba(255, 99, 132, 0.6)'
                    },
                    {
                        label: 'Compartlhamentos',
                        data: nota3Valores,
                        backgroundColor: 'rgba(54, 162, 235, 0.6)'
                    },
                    {
                        label: 'Engajamento',
                        data: mediaValores,
                        backgroundColor: 'rgba(255, 206, 86, 0.6)' // Yellow color
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                        
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Métricas de engajamento'
                    }
                }
            }
        });
    }
});