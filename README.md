<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>IPOAutomation</title>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

  <style>
    body { font-family: "Inter", sans-serif; }
  </style>
</head>
<body class="bg-gray-50 text-gray-900">

  <!-- Hero Section -->
  <header class="text-center py-20 bg-gradient-to-r from-blue-700 to-blue-500 text-white">
    <h1 class="text-4xl font-bold">🚀 IPOAutomation</h1>
    <p class="mt-3 text-lg opacity-90 max-w-2xl mx-auto">
      Automate IPO applications on the MeroShare platform — fast, reliable, and hassle-free.
    </p>

    <div class="mt-6 flex justify-center gap-4">
      <a href="docs/index.html" class="px-6 py-3 bg-white text-blue-600 font-semibold rounded-lg shadow hover:bg-gray-200">
        View Documentation
      </a>
      <a href="https://github.com/DesTnyLab/IPOAutomation" class="px-6 py-3 bg-gray-900 text-white font-semibold rounded-lg shadow hover:bg-gray-800">
        View Project
      </a>
    </div>
  </header>

  <!-- Features -->
  <section class="max-w-6xl mx-auto py-16 px-6">
    <h2 class="text-3xl font-semibold text-center mb-12">✨ Features</h2>

    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
      
      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">🔁 Automated IPO Application</h3>
        <p>Automatically apply for IPOs directly through MeroShare.</p>
      </div>

      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">👥 Multiple Accounts</h3>
        <p>Manage and apply from multiple DP accounts efficiently.</p>
      </div>

      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">🕒 Scheduled Applications</h3>
        <p>Run tasks automatically using Celery Beat scheduling.</p>
      </div>

      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">📊 Dashboard Monitoring</h3>
        <p>Track IPO status, history, and logs in one place.</p>
      </div>

      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">🔒 Secure Credentials</h3>
        <p>Stored safely using environment variables.</p>
      </div>

      <div class="p-6 bg-white rounded-xl shadow">
        <h3 class="font-semibold mb-2">⚙️ Asynchronous Processing</h3>
        <p>Celery ensures fast and stable background execution.</p>
      </div>

    </div>
  </section>

  <!-- Tech Stack -->
  <section class="bg-white py-16 px-6 shadow-inner">
    <h2 class="text-3xl font-semibold text-center mb-12">🛠️ Tech Stack</h2>

    <div class="max-w-4xl mx-auto">
      <table class="w-full border text-left border-gray-300 rounded-lg overflow-hidden">
        <thead class="bg-gray-100">
          <tr>
            <th class="p-3 border">Component</th>
            <th class="p-3 border">Technology Used</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="p-3 border">Backend</td><td class="p-3 border">Django</td></tr>
          <tr><td class="p-3 border">Database</td><td class="p-3 border">PostgreSQL</td></tr>
          <tr><td class="p-3 border">Task Queue</td><td class="p-3 border">Celery</td></tr>
          <tr><td class="p-3 border">Broker</td><td class="p-3 border">Redis</td></tr>
          <tr><td class="p-3 border">Frontend</td><td class="p-3 border">Django Templates</td></tr>
          <tr><td class="p-3 border">Deployment</td><td class="p-3 border">Docker / Nginx (Optional)</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- Footer -->
  <footer class="text-center py-10 mt-20 text-gray-600">
    © 2025 IPOAutomation — Built with ❤️ using Django & Celery
  </footer>

</body>
</html>
