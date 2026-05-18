const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};

    students.forEach((line) => {
      const student = line.split(',');
      const firstName = student[0];
      const field = student[3].trim();

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstName);
    });

    Object.keys(fields).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
