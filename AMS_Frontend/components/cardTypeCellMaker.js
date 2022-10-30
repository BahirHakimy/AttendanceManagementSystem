import Image from "next/image"
import Man from '../public/man.png'
const CardTypeCellMaker = ({cellData}) => {
  return (
    <div className="bg-slate-100">
            <Image src={ cellData.profile_pic ? `http://127.0.0.1:8000/${cellData.profile_pic}` : Man} width={100} height={100}/>

    </div>
  )
}

export default CardTypeCellMaker