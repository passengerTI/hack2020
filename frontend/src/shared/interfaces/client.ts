export interface Client {
	_id?: string;
	id?: string;
	areaType: string;
	birthday: string;
	age: string;
	diabet: string;
	diabet_long: string;
	ethnos: string;
	family: string;
	national: string;
	pension: string;
	profession: string
	religion: string;
	sex: string;
	study: string;
	work_end_by_ill: string;
	working: string;
	gipertenziya?: number;
	heart_failure?: number;
	infarkt?: number;
	onmk?: number;
	other_ill?: number;
}

export interface ClientFormData {
	client: Client | null;
}