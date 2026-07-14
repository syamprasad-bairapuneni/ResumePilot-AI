export default function Home() {
  return (
    <main className="min-h-screen bg-slate-100 flex items-center justify-center">
      <div className="w-full max-w-3xl bg-white rounded-xl shadow-lg p-8">

        <h1 className="text-4xl font-bold text-center mb-2">
          ResumePilot AI
        </h1>

        <p className="text-center text-gray-500 mb-8">
          AI Powered ATS Resume Builder
        </p>

        <div className="space-y-6">

          <div>
            <label className="block font-semibold mb-2">
              Upload Resume
            </label>

            <input
              type="file"
              className="w-full border rounded-lg p-3"
            />
          </div>

          <div>
            <label className="block font-semibold mb-2">
              Job Description
            </label>

            <textarea
              rows={10}
              className="w-full border rounded-lg p-3"
              placeholder="Paste Job Description here..."
            />
          </div>

          <button
            className="w-full bg-black text-white py-3 rounded-lg hover:bg-gray-800 transition"
          >
            Generate ATS Resume
          </button>

        </div>

      </div>
    </main>
  );
}