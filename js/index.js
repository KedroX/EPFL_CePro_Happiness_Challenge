const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../data/data-2019.csv');

// This function parses a plain CSV string and return an array of objects
const csvToJson = (csv) => {
    const lines = csv.split('\n');
    const headers = lines[0].split(',');

    return lines.slice(1).map(line => {
        const values = line.split(',');
        return headers.reduce((acc, header, index) => {
            acc[header.trim()] = values[index]?.trim();
            return acc;
        }, {});
    });
};

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    const jsonData = csvToJson(data);
    // Seems like one or more rows are empty, assuring to have clean data
    const filteredData = jsonData.filter(row => row['Country'] !== '');

    /* 1. Data summaries */
    const regionScores = {};
    filteredData.forEach(row => {
        const region = row['Region'];
        const score = parseFloat(row['Score 2019']);

        // Check if score is a valid number
        if (!isNaN(score)) {
            // If the region does not yet exists, creating it
            if (!regionScores[region]) {
                regionScores[region] = { total: 0, count: 0 };
            }
            regionScores[region].total += score;
            regionScores[region].count++;
        }
    });
    // Calculate average scores
    const averageScores = {};
    for (const region in regionScores) {
        const { total, count } = regionScores[region];
        averageScores[region] = total / count;
    }

    console.log('----------------------');
    console.log('Average Happiness Score by Region');
    console.log('----------------------');
    console.log(averageScores);
    
    // Sort countries by GDP
    const gdpSorted = filteredData.sort((a, b) => {
        const gdpA = parseFloat(a['GDP 2019']);
        const gdpB = parseFloat(b['GDP 2019']);

        if (isNaN(gdpA)) return 1;
        if (isNaN(gdpB)) return -1;

        return gdpB - gdpA;
    });

    // Top 10 countries by GDP
    console.log('----------------------');
    console.log('Top 10 countries by GDP');
    console.log('----------------------');
    for (let index = 0; index < 10; index++) {
        console.log(`${index + 1}. ${gdpSorted[index]['Country']}: ${gdpSorted[index]['GDP 2019']}`);
    }

    // Bottom 10 countries by GDP
    console.log('----------------------');
    console.log('Bottom 10 countries by GDP');
    console.log('----------------------');
    for (let index = gdpSorted.length - 1; index >= gdpSorted.length - 10; index--) {
        console.log(`${gdpSorted.length - index}. ${gdpSorted[index]['Country']}: ${gdpSorted[index]['GDP 2019']}`);
    }

    /* 2. Comparisons */

    // Pearson correlation, thanks to https://stackoverflow.com/a/41089665/
    const pearsonCorrelation = (x, y) => {
        let sumX = 0,
          sumY = 0,
          sumXY = 0,
          sumX2 = 0,
          sumY2 = 0;
        const minLength = x.length = y.length = Math.min(x.length, y.length),
          reduce = (xi, idx) => {
            const yi = y[idx];
            sumX += xi;
            sumY += yi;
            sumXY += xi * yi;
            sumX2 += xi * xi;
            sumY2 += yi * yi;
          }
        x.forEach(reduce);
        return (minLength * sumXY - sumX * sumY) / Math.sqrt((minLength * sumX2 - sumX * sumX) * (minLength * sumY2 - sumY * sumY));
    };

    const gdp = [];
    const score = [];
    // Crawling through the data to get the GDP and Score values
    filteredData.forEach(row => {
        const gdpValue = parseFloat(row['GDP 2019']);
        const scoreValue = parseFloat(row['Score 2019']);

        if (!isNaN(gdpValue) && !isNaN(scoreValue)) {
            gdp.push(gdpValue);
            score.push(scoreValue);
        }
    });
    const correlation = pearsonCorrelation(gdp, score);
    console.log('----------------------');
    console.log('Correlation between GDP and Happiness Score:', correlation);
    console.log('----------------------');

});