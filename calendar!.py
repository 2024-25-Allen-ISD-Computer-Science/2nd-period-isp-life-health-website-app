<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fitness Tracker Calendar</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #e6f0ff;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: inline-block;
            width: 80%;
            max-width: 800px;
        }
        input, select {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1.1em;
        }
        button {
            padding: 10px 20px;
            font-size: 1.1em;
            color: white;
            background-color: #0073e6;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 10px;
        }
        button:hover {
            background-color: #005bb5;
        }
        #result {
            margin-top: 20px;
            font-size: 1.2em;
            font-weight: bold;
            color: #0073e6;
        }
        .calendar {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 5px;
            margin-top: 20px;
        }
        .calendar .day {
            padding: 20px;
            background-color: #f0f8ff;
            border-radius: 5px;
            cursor: pointer;
        }
        .calendar .day:hover {
            background-color: #e0e7ff;
        }
        .calendar .active {
            background-color: #0073e6;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fitness Tracker Calendar</h1>
        <p>Select a date to log your fitness activity:</p>

        <!-- Calendar will be dynamically generated here -->
        <div class="calendar" id="calendar"></div>

        <br>
        <div>
            <input type="text" id="activity" placeholder="Enter your fitness activity">
            <button onclick="logActivity()">Log Activity</button>
        </div>
        
        <p id="result"></p>
        
        <br>
        <a href="index.html"><button>Back to Home</button></a>
    </div>

    <script>
        const activities = {}; // Store activities with date as key
        
        // Generate the calendar for the current month
        function generateCalendar() {
            const calendarDiv = document.getElementById('calendar');
            calendarDiv.innerHTML = ''; // Clear existing calendar

            const currentDate = new Date();
            const currentMonth = currentDate.getMonth();
            const currentYear = currentDate.getFullYear();
            const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
            const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);

            const startDay = firstDayOfMonth.getDay();
            const totalDays = lastDayOfMonth.getDate();

            // Create empty slots for the days before the first of the month
            for (let i = 0; i < startDay; i++) {
                const emptySlot = document.createElement('div');
                calendarDiv.appendChild(emptySlot);
            }

            // Create day elements
            for (let day = 1; day <= totalDays; day++) {
                const dayDiv = document.createElement('div');
                dayDiv.classList.add('day');
                dayDiv.textContent = day;
                dayDiv.dataset.date = `${currentYear}-${currentMonth + 1}-${day}`;

                // Add event listener for clicking on a day
                dayDiv.addEventListener('click', () => selectDay(dayDiv));

                calendarDiv.appendChild(dayDiv);
            }
        }

        // Select a day and highlight it
        function selectDay(dayDiv) {
            const selectedDay = document.querySelector('.active');
            if (selectedDay) {
                selectedDay.classList.remove('active');
            }
            dayDiv.classList.add('active');
        }

        // Log fitness activity for the selected day
        function logActivity() {
            const activityInput = document.getElementById('activity');
            const selectedDay = document.querySelector('.active');
            const resultText = document.getElementById('result');
            
            if (selectedDay && activityInput.value) {
                const date = selectedDay.dataset.date;
                activities[date] = activityInput.value; // Store activity for that date
                
                resultText.textContent = `Activity for ${date} logged: ${activities[date]}`;
                activityInput.value = ''; // Clear the input
            } else {
                resultText.textContent = 'Please select a day and enter an activity.';
            }
        }

        // Initialize the calendar
        generateCalendar();
    </script>
</body>
</html>
