"use client";
import { Alert } from "flowbite-react";
import { Navbar } from "../components/navbar";
import { Footer } from "../components/footer";
export default function Home() {
  return (
    <>
      <Navbar />
      <Alert color="info">Alert!</Alert>;
      <div className="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700" >
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Simple, <mark className="px-2 text-white bg-blue-600 rounded dark:bg-blue-500">private</mark> file sharing</h1>
      </div>
      <Footer /> 
    </> 
  )
};
