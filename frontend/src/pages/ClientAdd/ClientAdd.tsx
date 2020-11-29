import React, {useState} from 'react';
import ClientForm from './../../shared/components/ClientForm'
import './styles.scss';
import {Client} from '../../shared/interfaces/client';

const ClientAdd = () => {
  const [client, setClient] = useState<Client>({
    areaType: '1',
    birthday: '',
    age: '24',
    diabet: '0',
    diabet_long: '0',
    ethnos: 'русский',
    family: 'женат',
    national: 'европейская',
    pension: '0',
    profession: 'программист',
    religion: 'атеист',
    sex: 'М',
    study: 'высшее',
    work_end_by_ill: '0',
    working: '1'
  });

  return (
    <div>
      Новая анкета
      <ClientForm
        client={client}
      />
    </div>
  )
}

export default ClientAdd
