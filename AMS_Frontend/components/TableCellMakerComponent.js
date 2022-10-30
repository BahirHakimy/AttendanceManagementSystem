
const TableCellMaker = ({cellData,idx}) => {
  return (
    <tr className="hover:bg-darkShadeCyan hover:text-white hover:cursor-pointer">
        <td>{idx+1}</td>
        <td>{cellData.user.username}</td>
        <td>{cellData.user.first_name}</td>
        <td>{cellData.user.last_name}</td>
        <td>{cellData.degree}</td>
    </tr>
  )
}

export default TableCellMaker