"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [resumeData, setResumeData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function uploadResume() {
    if (!file) {
      alert("Please choose a resume.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await api.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setResumeData(response.data.data);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-100 flex justify-center p-10">
      <div className="w-full max-w-4xl bg-white rounded-xl shadow-lg p-8">

        <h1 className="text-4xl font-bold text-center">
          ResumePilot AI
        </h1>

        <p className="text-center text-gray-500 mt-2 mb-8">
          AI Powered ATS Resume Builder
        </p>

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files ? e.target.files[0] : null)
          }
          className="mb-5"
        />

        <button
          onClick={uploadResume}
          className="bg-black text-white px-6 py-3 rounded-lg"
        >
          {loading ? "Uploading..." : "Upload Resume"}
        </button>

        {resumeData && (
          <div className="mt-10 border rounded-lg p-6">

            <h2 className="text-2xl font-bold mb-4">
              Parsed Resume
            </h2>

            <pre className="overflow-auto text-sm">
              {JSON.stringify(resumeData, null, 2)}
            </pre>

          </div>
        )}

      </div>
    </main>
  );
}