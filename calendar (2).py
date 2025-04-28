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
    </style>
</head>
<body>
    <div class="container">
        <h1>Fitness Tracker Calendar</h1>
        <p>Select your fitness activities from the calendar:</p>

        <!-- Embed Dash App here, this can be an iframe that points to your Dash app URL -->
        <iframe src="http://localhost:8050" width="100%" height="600px" style="border: none;"></iframe>

        <br>
        <a href="index.html"><button>Back to Home</button></a>
    </div>
</body>
</html>
