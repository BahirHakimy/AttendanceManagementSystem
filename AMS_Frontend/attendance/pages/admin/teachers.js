import { useRouter } from 'next/router'
import React from 'react'

const TeacherPanel = () => {
    const router = useRouter();
    console.log(router);
  return (
    <div>TeacherPanel</div>
  )
}

export default TeacherPanel